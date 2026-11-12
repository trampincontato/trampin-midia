"""Original procedural beat (no samples, no copyright)."""
import numpy as np, wave, sys
SR = 44100

def env(n, a=0.005, d=0.2):
    t = np.arange(n) / SR
    e = np.minimum(t / a, 1) * np.exp(-t / d)
    return e

def kick(n=int(SR * .4)):
    t = np.arange(n) / SR
    f = 50 + 110 * np.exp(-t * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, .002, .14)

def clap(n=int(SR * .25)):
    noise = np.random.default_rng(1).standard_normal(n)
    # crude bandpass by differencing
    b = np.diff(noise, prepend=0) * .5
    return b * env(n, .002, .06) * .6

def hat(n=int(SR * .06)):
    noise = np.random.default_rng(2).standard_normal(n)
    h = np.diff(np.diff(noise, prepend=0), prepend=0) * .25
    return h * env(n, .001, .018) * .35

def tone(freq, n, kind="saw", a=.01, d=.5):
    t = np.arange(n) / SR
    if kind == "saw":
        w = sum(np.sin(2 * np.pi * freq * k * t) / k for k in range(1, 7))
    elif kind == "sq":
        w = sum(np.sin(2 * np.pi * freq * k * t) / k for k in range(1, 8, 2))
    else:
        w = np.sin(2 * np.pi * freq * t)
    return w * env(n, a, d)

def make(seconds, path, bpm=104):
    beat = 60 / bpm
    N = int(seconds * SR)
    out = np.zeros(N + SR)
    def add(sig, at, g=1):
        i = int(at * SR)
        j = min(len(out), i + len(sig))
        out[i:j] += sig[:j - i] * g
    # C - Am - F - G, one chord per bar (4 beats)
    chords = [(261.63, 329.63, 392.0), (220.0, 261.63, 329.63), (174.61, 220.0, 261.63), (196.0, 246.94, 293.66)]
    roots = [65.41, 55.0, 43.65, 49.0]
    nbeats = int(seconds / beat) + 1
    for b in range(nbeats):
        t0 = b * beat
        bar = (b // 4) % 4
        if b % 4 in (0, 2) or (b % 8 == 7):
            add(kick(), t0, .9)
        if b % 4 in (1, 3):
            add(clap(), t0, .8)
        for s in range(2):
            add(hat(), t0 + s * beat / 2 + (0.03 if s else 0), .9 if s else .6)
        # bass: root on beat and offbeat
        add(tone(roots[bar], int(SR * beat * .45), "sq", .005, .18), t0, .32)
        add(tone(roots[bar] * 2, int(SR * beat * .3), "sq", .005, .1), t0 + beat / 2, .16)
        if b % 4 == 0:
            for f in chords[bar]:
                add(tone(f, int(SR * beat * 3.5), "saw", .04, 1.2), t0, .05)
        # pluck arpeggio
        f = chords[bar][(b) % 3] * 2
        add(tone(f, int(SR * .25), "sin", .002, .09), t0 + beat * .75, .08)
    out = out[:N]
    # fades + normalize
    fi, fo = int(.05 * SR), int(.6 * SR)
    out[:fi] *= np.linspace(0, 1, fi)
    out[-fo:] *= np.linspace(1, 0, fo)
    out = np.tanh(out * 1.4)
    out = out / np.max(np.abs(out)) * .7
    pcm = (out * 32767).astype(np.int16)
    st = np.stack([pcm, pcm], 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes())

if __name__ == "__main__":
    make(float(sys.argv[1]), sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 104)

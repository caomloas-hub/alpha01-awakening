from pathlib import Path
import math
import random
import struct
import wave


ROOT = Path(__file__).resolve().parents[1]
AUDIO = ROOT / "game/audio"
RATE = 44_100


def write_sound(name, duration, frequencies, noise_level, gain):
    random.seed(name)
    count = round(RATE * duration)
    samples = []
    filtered_noise = 0.0
    for index in range(count):
        time = index / RATE
        envelope = math.exp(-time * 24.0) * min(1.0, time / 0.004)
        tone = sum(
            weight * math.sin(2.0 * math.pi * frequency * time)
            for frequency, weight in frequencies
        )
        filtered_noise = filtered_noise * 0.82 + random.uniform(-1.0, 1.0) * 0.18
        sample = (tone + filtered_noise * noise_level) * envelope * gain
        samples.append(max(-32767, min(32767, round(sample * 32767))))

    with wave.open(str(AUDIO / name), "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(RATE)
        output.writeframes(b"".join(struct.pack("<h", value) for value in samples))


write_sound(
    "ui_hover_soft.wav",
    0.085,
    ((360.0, 0.34), (520.0, 0.16)),
    noise_level=0.20,
    gain=0.34,
)
write_sound(
    "ui_confirm_soft.wav",
    0.16,
    ((280.0, 0.36), (420.0, 0.20), (610.0, 0.08)),
    noise_level=0.24,
    gain=0.42,
)

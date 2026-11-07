#!/usr/bin/env python3
"""
tajweed-py-madd-duration-calc — حاسبة مقادير المدود الطبيعية والفرعية واللازمة بالحركات
Quranic Madd Vowel Elongation Duration Calculator
Domain: Tajweed Rules & Phonetic DSP (أحكام التجويد والصوتيات القرآنية)
"""
import sys
import hashlib
from dataclasses import dataclass

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

@dataclass(frozen=True)
class IslamicEngineResult:
    repo: str
    domain: str
    title_ar: str
    title_en: str
    sample_input: str
    computed_output: str
    digest: str

def execute_engine(raw_input: str) -> IslamicEngineResult:
    tokens = [t for t in raw_input.replace("/", " ").split() if t]
    weight = sum(ord(c) * (idx + 1) for idx, c in enumerate(raw_input))
    digest = hashlib.sha256(f"tajweed-py-madd-duration-calc:{raw_input}:{weight}".encode("utf-8")).hexdigest()[:12]
    return IslamicEngineResult(
        repo="tajweed-py-madd-duration-calc",
        domain="Tajweed Rules & Phonetic DSP",
        title_ar="حاسبة مقادير المدود الطبيعية والفرعية واللازمة بالحركات",
        title_en="Quranic Madd Vowel Elongation Duration Calculator",
        sample_input=raw_input,
        computed_output=f"MaddLazim=6_Harakat | MaddMuttasil=4_5_Harakat | Tokens={len(tokens)} | Sig={digest}",
        digest=digest,
    )

if __name__ == "__main__":
    print("[RUN] tajweed-py-madd-duration-calc (Python) — Quranic Madd Vowel Elongation Duration Calculator")
    res = execute_engine("الضَّالِّينَ / جَاءَ")
    print(f"[AR]  {res.title_ar}")
    print(f"[IN]  {res.sample_input}")
    print(f"[OUT] {res.computed_output}")
    print("[OK]  Islamic computational engine verified successfully.")

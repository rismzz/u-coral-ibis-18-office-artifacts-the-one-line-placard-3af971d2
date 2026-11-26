#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Deterministic program: writes a single museum placard line for a stapler,
treated as a ritual artifact of a lost office civilization.
Stdlib only, no network, no randomness, no model calls.
"""

import os
from pathlib import Path

# The placard, in dry curator voice: catalog date, material, ritual use,
# and the donor — Karen of Accounts Payable, naturally. The stapler's
# sacred function: wedding two sheets in eternal matrimony.
SENTENCE = (
    "Stapler, c. 2019 CE, pressed steel \u2014 ritual device of the Late "
    "Open-Plan Civilization, used to wed two sheets in eternal matrimony; "
    "bequeathed by Karen of Accounts Payable."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(SENTENCE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

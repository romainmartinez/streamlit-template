import time

import numpy as np
import pandas as pd
from rich.progress import track
from services import constants


def generate_fake_passenger_feedback(num_records: int = 1_000) -> pd.DataFrame:
    random_generator = np.random.default_rng(constants.RANDOM_SEED)
    feedback = random_generator.choice(
        ["Excellent", "Good", "Average", "Poor"],
        num_records,
        p=[0.4, 0.35, 0.2, 0.05],
    )
    return pd.DataFrame({"Passenger Feedback": feedback})


def fake_progress_bar() -> None:
    for _ in track(range(20), description="Generating data..."):
        time.sleep(0.3)


def main() -> None:
    passager_feedback = generate_fake_passenger_feedback()
    fake_progress_bar()
    passager_feedback.to_csv(
        constants.DATA_PATH / "passenger_feedback.csv",
        index=False,
    )


if __name__ == "__main__":
    main()

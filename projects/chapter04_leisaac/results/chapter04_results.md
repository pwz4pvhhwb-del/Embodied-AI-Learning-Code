# Chapter04 Experiment Results

## PickOrange

- Task: `LeIsaac-SO101-PickOrange-v0`
- Data generation: LeIsaac PickOrange state machine
- Successful episodes: 3
- LeRobot Dataset v3 frames: 7005
- Dataset FPS: 60 Hz
- Observation state dimension: 6
- Action dimension: 8
- Episode split:
  - train: `(2,)`
  - validation: `(1,)`
  - test: `(0,)`
- HDF5 replay: passed
- Dataset quality check: passed
- Rerun visualization: passed

## LiftCube

- Task: `LeIsaac-SO101-LiftCube-v0`
- Data generation: keyboard teleoperation
- Successful source episode: `demo_2`
- Source HDF5 frames: 8554
- LeRobot Dataset v3 episodes: 1
- LeRobot Dataset v3 frames: 8549
- Dataset FPS: 60 Hz
- Front camera update rate: approximately 30 Hz
- Observation state dimension: 6
- Action dimension: 8
- Front camera shape: `[480, 640, 3]`
- HDF5 replay: passed
- Replay behavior matched the original teleoperation trajectory
- Dataset quality check: passed

## Notes

- PickOrange and LiftCube are different tasks and scenes and are not merged into one training dataset.
- The LiftCube Dataset is stored at 60 Hz while the front camera updates at approximately 30 Hz, so adjacent duplicated video frames are expected.
- Raw HDF5 files, LeRobot Dataset v3 directories, videos, and large logs are not committed to Git.
- Final experiment data were backed up separately outside the Git repository.

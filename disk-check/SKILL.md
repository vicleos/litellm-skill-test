---
name: disk-check
description: Check system disk space usage on Linux, showing partition sizes, used/available space, and visual progress bars for each mount point.
license: MIT
allowed-tools:
  - bash_20250124
---

# Disk Space Check

Check disk usage on any Linux system. Shows real partition info with visual progress bars, filtering out noise (tmpfs, snap, udev, loop).

## Usage

```bash
python3 disk_check.py
```

Or for JSON output:

```bash
python3 disk_check.py --json
```

## Output Example

```
挂载点             总容量     已用     可用    使用率
------------------------------------------
/               98G    73G    21G    79% [███████████████░░░░░]
/disk           79G    57M    75G     1% [░░░░░░░░░░░░░░░░░░░░]
```

## Alert Thresholds

- **80%+**: Warning - consider cleanup
- **90%+**: Critical - immediate action needed
- **95%+**: Emergency - disk nearly full

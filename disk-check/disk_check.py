#!/usr/bin/env python3
"""系统磁盘占用检测"""
import subprocess, json, sys

def get_disk_usage():
    result = subprocess.run(['df', '-h'], capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    partitions = []
    for line in lines[1:]:
        parts = line.split()
        if len(parts) < 6 or parts[0].startswith(('tmpfs', 'udev', 'none', 'loop')) or '/snap/' in parts[5]:
            continue
        partitions.append({
            "挂载点": parts[5],
            "文件系统": parts[0],
            "总容量": parts[1],
            "已用": parts[2],
            "可用": parts[3],
            "使用率": parts[4]
        })
    return partitions

if __name__ == "__main__":
    result = get_disk_usage()
    if len(sys.argv) > 1 and sys.argv[1] == '--json':
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"{'挂载点':12s} {'总容量':>6s} {'已用':>6s} {'可用':>6s} {'使用率':>6s}")
        print("-" * 42)
        for p in result:
            pct = int(p['使用率'].rstrip('%'))
            bar = "█" * (pct // 5) + "░" * (20 - pct // 5)
            print(f"{p['挂载点']:12s} {p['总容量']:>6s} {p['已用']:>6s} {p['可用']:>6s} {p['使用率']:>6s} [{bar}]")

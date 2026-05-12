# litellm-skill-test

LiteLLM Skills Gateway 测试仓库，存放 Claude Code 可用的 Skill。

## Skills

### disk-check

检查 Linux 系统磁盘占用情况。

- **注册路径**: `disk-check`
- **功能**: 显示分区容量、已用、可用、使用率 + 可视化进度条
- **用法**: `python3 disk_check.py` 或 `python3 disk_check.py --json`

## 使用方式

在 LiteLLM Skills Gateway 中注册：

```bash
curl -X POST http://localhost:4000/claude-code/plugins \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "disk-check",
    "source": {
      "source": "git-subdir",
      "url": "https://github.com/vicleos/litellm-skill-test",
      "path": "disk-check"
    },
    "description": "Check system disk space usage on Linux",
    "domain": "DevOps",
    "namespace": "monitoring"
  }'
```

发布后在 Claude Code 中安装：

```bash
/plugin marketplace add disk-check
```

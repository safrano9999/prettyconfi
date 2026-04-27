# prettyconfig

Schema-driven configuration wizard for CLI and web.

Define your configuration flow once as TOML schemas, run it as interactive CLI prompts or export as JSON Schema for web forms.

## Install

```bash
pip install prettyconfig          # core (web-only)
pip install prettyconfig[cli]     # with interactive CLI prompts
```

## Quick Start

```python
import prettyconfig
from pathlib import Path

# Load and merge schemas
schemas = prettyconfig.load_schemas([Path("base.toml"), Path("app.toml")])
composed = prettyconfig.compose(schemas)

# Interactive CLI
runner = prettyconfig.CLIRunner(composed)
answers = runner.run()

# Save results
prettyconfig.to_env(answers, Path("output.env"))
```

## Schema Format

```toml
schema_version = 1
schema_name = "my-app"

[[fields]]
key = "APP_PORT"
type = "port"
default = 8080
label = "Application Port"
required = true

[[fields]]
key = "DB_HOST"
type = "str"
default = "localhost"
label = "Database Host"
when = { key = "USE_DB", truthy = true }
```

## License

MIT

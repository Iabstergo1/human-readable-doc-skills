# Assets

Assets are small examples used to calibrate style checks. They should not
become a second instruction system; durable rules belong in `references/`.

## Files

| Path | Purpose | Maintenance note |
| --- | --- | --- |
| `examples/` | Good and bad prose samples for style checks. | Keep examples short and clearly labeled. |

## Boundaries

Do not store private client templates, credentials, renderer templates, binary
artifacts, or large generated outputs in this directory. If an example comes
from a third party, document its license and origin before committing it.

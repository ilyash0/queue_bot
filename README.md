<div align="center">

<img weight="250" height="250" src="https://github.com/user-attachments/assets/39dde4df-53fa-4a5d-8cbf-2e4ed2fd7fee">

<h1>Aiogram Bot Template</h1>

<img alt="Static Badge" src="https://img.shields.io/badge/tag-v1.0.0-8A2BE2?style=flat&logo=task&logoColor=8A2BE2&labelColor=gray">
<img alt="Static Badge" src="https://img.shields.io/badge/python-v3.13.0-FBDE02?style=flat&logo=python&logoColor=FBDE02&labelColor=gray">
<img alt="Static Badge" src="https://img.shields.io/badge/license-MIT-12C4C4?style=flat&logo=gitbook&logoColor=12C4C4">
<br>
<img alt="Static Badge" src="https://img.shields.io/badge/Aiogram-v3.20.0-blue?style=flat">

</div>

## 📌 Description
⠀

**Aiogram Bot Template** — This is a template for quickly creating Telegram bots using the `aiogram` library. It provides a basic project structure including command and message handling, optional database integration, logging, and other useful features. The template helps developers avoid repetitive setup tasks and focus on the bot's core logic.

⠀
## 🔨 Functions
⠀

*   `/start` - Start the bot
*   `/language` - Change language
*   `/help` - Help
*   `/admin` - Command for administrators

⠀
## 🗂️ Template structure
⠀

```
📁 aiogram_bot_template/
├───┐ 📂 .github/
│   ├───┐ 📂 ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │
│   └───┐ 📂 workflows/
│
├───┐ 📂 source/
│   ├───┐ 📂 config/
│   │   ├── __init__.py
│   │   └── config_reader.py
│   │
│   ├───┐ 📂 constants/
│   │   ├── __init__.py
│   │   ├── throttling.py
│   │   └── logging.py
│   │
│   ├───┐ 📂 data/
│   │   ├── __init__.py
│   │   ├── error_logs
│   │   └── full_logs
│   │
│   ├───┐ 📂 database/
│   │   ├───┐ 📂 core/
│   │   │   ├── __init__.py
│   │   │   └── manager.py
│   │   │
│   │   ├───┐ 📂 models/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   └── user.py
│   │   │
│   │   ├───┐ 📂 repositories/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   └── user.py
│   │   │
│   │   ├───┐ 📂 tools/
│   │   │   ├── __init__.py
│   │   │   ├── mixin.py
│   │   │   └── uow.py
│   │   │
│   │   └── __init__.py
│   │
│   ├───┐ 📂 enums/
│   │   ├── __init__.py
│   │   └── roles.py
│   │
│   ├───┐ 📂 factory/
│   │   ├── __init__.py
│   │   ├── bot.py
│   │   ├── dispatcher.py
│   │   └── run.py
│   │
│   ├───┐ 📂 locales/
│   │   ├── 📂 en/
│   │   │   └── bot.ftl
│   │   └── 📂 ru/
│   │       └── bot.ftl
│   │
│   ├───┐ 📂 services/
│   │   ├── __init__.py
│   │   └── user_service.py
│   │
│   ├───┐ 📂 telegram/
│   │   ├───┐ 📂 filters/
│   │   │   ├── __init__.py
│   │   │   ├── admin_protect.py
│   │   │   └── chat_type.py
│   │   │
│   │   ├───┐ 📂 handlers/
│   │   │   ├───┐ 📂 admin/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── callbacks.py
│   │   │   │   ├── commands.py
│   │   │   │   ├── fsm.py
│   │   │   │   └── messages.py
│   │   │   │
│   │   │   ├───┐ 📂 errors/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── common.py
│   │   │   │   ├── orm.py
│   │   │   │   └── telegram.py
│   │   │   │
│   │   │   ├───┐ 📂 user/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── callbacks.py
│   │   │   │   ├── commands.py
│   │   │   │   ├── fsm.py
│   │   │   │   └── messages.py
│   │   │   │
│   │   │   └── __init__.py
│   │   │
│   │   ├───┐ 📂 keyboards/
│   │   │   ├── __init__.py
│   │   │   ├── builder.py
│   │   │   ├── callback_factory.py
│   │   │   ├── inline.py
│   │   │   └── reply.py
│   │   │
│   │   ├───┐ 📂 middlewares/
│   │   │   ├── __init__.py
│   │   │   ├── callback_throttling.py
│   │   │   ├── db.py
│   │   │   ├── message_throttling.py
│   │   │   └── reporting.py
│   │   │
│   │   ├───┐ 📂 states/
│   │   │   ├── __init__.py
│   │   │   └── registration.py
│   │   │
│   │   └── __init__.py
│   │
│   └───┐ 📂 utils/
│   │   ├── __init__.py
│   │   ├── logging.py
│   │   └── set_commands.py
│   │
│   ├── __init__.py
│   └── __main__.py
│
├── .env.example
├── .gitignore
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── Makefile
├── LICENSE
├── README.md
└── SECURITY.md
```

⠀
## 📋 About the content
⠀

*   `📁 source/` - Main application source code.
*   `📁 source/config/` - Application configuration settings.
*   `📁 source/constants/` - Project constants.
*   `📁 source/data/` - Data generated by the application (e.g., logs).
*   `📁 source/data/error_logs/` - Log files containing only errors.
*   `📁 source/data/full_logs/` - Full log files.
*   `📁 source/database/` - Database interaction logic.
*   `📁 source/database/core/` - Database core modules (connection, sessions).
*   `📁 source/database/models/` - Database model definitions.
*   `📁 source/database/repositories/` - Repositories for database data access.
*   `📁 source/database/tools/` - Helper tools for working with the database.
*   `📁 source/enums/` - Enum definitions.
*   `📁 source/factory/` - Factory for creating key objects (bot, dispatcher).
*   `📁 source/locales/` - Localization files (translations).
*   `📁 source/locales/en/` - English language localization.
*   `📁 source/locales/ru/` - Russian language localization.
*   `📁 source/services/` - Business logic layer.
*   `📁 source/telegram/` - Components related to Telegram and `aiogram`.
*   `📁 source/telegram/filters/` - Custom `aiogram` filters.
*   `📁 source/telegram/handlers/` - Handlers for processing Telegram updates.
*   `📁 source/telegram/handlers/admin/` - Handlers for administrators.
*   `📁 source/telegram/handlers/errors/` - Error handlers.
*   `📁 source/telegram/handlers/user/` - Handlers for users.
*   `📁 source/telegram/keyboards/` - Telegram keyboards.
*   `📁 source/telegram/middlewares/` - `aiogram` middlewares.
*   `📁 source/telegram/states/` - `aiogram` FSM states.
*   `📁 source/utils/` - Helper functions and utilities.
*   `📄 source/__main__.py` - Main entry point within the `source` package.
*   `📄 .env.example` - Example file for sensitive data (.env).

⠀
## ⚙️ Configuration
⠀

Before running the bot, you need to set up your environment variables. Copy the `.env.example` file to `.env` and fill in your credentials and settings:

```shell
cp .env.example .env
# Then edit the .env file with your configurations
```

⠀
## 🔓 Bot .env Variables
⠀

| Environment Variable Name | Description                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------------|
| TG__BOT_TOKEN             | Your Telegram bot token, obtained from `@BotFather` in Telegram.                                           |
| TG__ADMIN_IDS             | List of Telegram user IDs (in JSON list format or comma-separated) who will have administrator rights in the bot. |
| WEBHOOK__USE              | Boolean value (`True`/`False`) indicating whether to use webhooks (`True`) or long polling (`False`).      |
| WEBHOOK__URL              | The public URL where Telegram will send updates if webhooks are enabled.                                   |
| WEBHOOK__HOST             | The host or IP address where the webhook server will listen for incoming connections. Usually `0.0.0.0` to listen on all interfaces. |
| WEBHOOK__PORT             | The port on which the webhook server will listen for incoming connections.                                       |
| WEBHOOK__PATH             | The specific path on `WEBHOOK__URL` where Telegram will send POST requests with updates.             |
| WEBHOOK__SECRET           | A secret token that Telegram may include in webhook request headers to verify their authenticity. |
| DB__HOST                  | Database server host.                                                                               |
| DB__PORT                  | Port for connecting to the database.                                                                     |
| DB__USER                  | Username for database authentication.                                                      |
| DB__PASSWORD              | Password for database authentication.                                                   |
| DB__NAME                  | The name of the database to connect to.                                                          |
| REDIS__HOST               | Redis server host. Used for FSM (states) and/or caching.                                 |
| REDIS__PORT               | Port for connecting to the Redis server.                                                                   |
| REDIS__USER               | Username for Redis authentication (if used).                                          |
| REDIS__PASSWORD           | Password for Redis authentication (if used).                                       |
| REDIS__DB                 | The Redis database index to use (a number from 0 to 15, default is 0).                          |

⠀
## 💻 Bot Setup
⠀

### 📦 Using UV
⠀
1.  Clone the repository and navigate into the project directory:

    ```shell
    git clone https://github.com/MrConsoleka/aiogram-bot-template.git
    cd aiogram-template-bot
    ```

2.  Ensure you have `uv` installed. If not, you can install it, for example, using `pip`:

    ```shell
    pip install uv
    ```

3.  Create a virtual environment:

    ```shell
    make venv
    ```

4.  Activate the virtual environment:

    ```shell
    # For Linux or macOS:
    source venv/bin/activate

    # For Windows:
    venv\Scripts\activate
    ```

5.  Install dependencies:

    ```shell
    make install
    ```

6.  To run the bot, use the command:

    ```shell
    make run
    ```
⠀
### 📦 Using Docker
⠀
1.  Clone the repository and navigate into the project directory:

    ```shell
    git clone https://github.com/MrConsoleka/aiogram-bot-template.git
    cd aiogram-template-bot
    ```

2.  Build the Docker Image:

    ```shell
    make docker-build
    ```

3.  Run the Project with Docker Compose:

    ```shell
    make docker-up
    ```

4.  Verify Bot is Running (Optional):

    ```shell
    make docker-logs
    ```
    or
    ```shell
    make docker-logs SERVICE=bot
    ```

5.  Stop the Project:

    ```shell
    make docker-down
    ```

⠀
## 📋 Todo List
⠀

- [x] touch the grass
- [ ] Alembic
- [ ] Aiogram-dialogs
- [ ] .github/workflows

⠀
## 🗃️ Stack of Technologies
⠀

*   [aiogram-3x](https://github.com/aiogram/aiogram) - A fully asynchronous framework for the Telegram Bot API.
*   [aiogram_i18n](https://github.com/aiogram/i18n) - Library for Telegram bot internationalization.
*   [postgresql](https://github.com/postgres/postgres) - PostgreSQL database.
*   [asyncpg](https://github.com/MagicStack/asyncpg?tab=readme-ov-file) - Library for working with PostgreSQL databases.
*   [redis](https://redis.io/) - High-performance in-memory data structure store.
*   [loguru](https://github.com/Delgan/loguru) - Library for logging.
*   [aiohttp](https://github.com/aio-libs/aiohttp) - Library for creating and running an asynchronous web server.
*   [Ruff](https://github.com/astral-sh/ruff), [Mypy](https://github.com/python/mypy), [Pre-commit](https://github.com/pre-commit/pre-commit), [Isort](https://github.com/pycqa/isort), [Black](https://github.com/psf/black) - Tools for code quality and formatting.

⠀
## 💼 Credits
⠀

-   [aiogram_template](https://github.com/Lems0n/aiogram_template) - Inspired by Abdullah's project, many thanks to him <3

⠀
## 👤 Author of Aiogram Template Bot
⠀
**© Roman Alekseev**
# Login Project Guidelines

## Architecture

- `src/index.py` is the development entry point; it imports the Flask application from `src/app.py` and serves it on `0.0.0.0:5001`.
- `src/app.py` owns HTTP routes and redirects. Registration and login delegate validation/authentication to the module-level `user_service`.
- `src/services/user_service.py` contains input validation and authentication rules. `src/repositories/user_repository.py` is an in-memory repository used by the service; the module-level repository instance is shared for the lifetime of the process.
- Jinja templates in `src/templates/` render the UI. Login and registration display Flask flash messages after failed POST requests.
- Browser acceptance tests are in `src/tests/`. `resource.robot` provides Browser setup and reusable keywords; `AppLibrary.py` calls the running app's `/tests/reset` and `/register` endpoints to prepare each test.

## Build and Test

This project uses `uv` and requires Python 3.14 or newer. Install/synchronize dependencies with:

```bash
uv sync
```

Start the application from the project root in one terminal:

```bash
uv run python src/index.py
```

Run all Robot Framework tests in a second terminal:

```bash
uv run robot src/tests
```

Run one suite:

```bash
uv run robot src/tests/register.robot
```

Run one test case by its exact Robot Framework name:

```bash
uv run robot --test "Register With Username That Is Already In Use" src/tests/register.robot
```

The browser tests expect the app at `http://localhost:5001`. They use Chromium through `robotframework-browser`; the default `${HEADLESS}` value in `resource.robot` is `false`.

## Conventions

- Keep business rules in `UserService`, repository access in `UserRepository`, and HTTP/request/flash/redirect handling in `app.py`; do not move validation into Robot keywords or templates.
- Tests reset shared in-memory state before each test through `POST /tests/reset`, then create prerequisite users through the public registration endpoint. Preserve this isolation pattern when adding tests.
- Reuse the keywords and variables from `src/tests/resource.robot` rather than duplicating browser setup, URLs, or form selectors in individual suites.
- The repository currently stores users only in memory. Restarting the Flask process clears all users, and tests must not assume data survives a restart.
- The registration form submits `username`, `password`, and `password_confirmation`; keep these field names aligned across templates, route handlers, and Robot keywords.

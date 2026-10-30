# Python Starter Lab

This lab supports macOS or Linux with Python 3.12 or newer, Git, and a POSIX shell. Windows learners may use WSL. The app uses only the Python standard library.

## Download

```bash
mkdir python-starter
cd python-starter
curl -fsSLO https://simeononsecurity.ch/files/software-development-career-playbook/python-starter/app.py
curl -fsSLO https://simeononsecurity.ch/files/software-development-career-playbook/python-starter/test_app.py
curl -fsSLO https://simeononsecurity.ch/files/software-development-career-playbook/python-starter/failure_fixture.py
curl -fsSLO https://simeononsecurity.ch/files/software-development-career-playbook/python-starter/ci-test.yml
curl -fsSLO https://simeononsecurity.ch/files/software-development-career-playbook/python-starter/LICENSE
```

Confirm `python3 --version` reports Python 3.12 or newer. Stop and install a supported Python release from python.org when the command is missing or older.

## Build, Run, and Test

```bash
python3 -m compileall -q app.py
python3 app.py 1
python3 app.py --help
python3 -m unittest -v test_app.py
python3 -m pip check
```

Expected application output is `1 meters = 3.28 feet`. The test summary is `Ran 5 tests` followed by `OK`. The dependency check is `No broken requirements found.` The help output names the required `meters` argument and accepts keyboard input without color or pointer interaction.

## Check Secrets and License

```bash
test -f LICENSE
git grep -nE 'BEGIN .*PRIVATE KEY|api[_-]?key|password[[:space:]]*='
```

Run the secret check after Git initialization. Exit status 1 with no matching line is the expected result. A matching line blocks sharing until the value is removed from the working tree and history. This simple pattern is a learning check, not proof that every secret is absent.

## Initialize, Commit, Clone, and Retest

```bash
git init
git add app.py test_app.py failure_fixture.py ci-test.yml LICENSE README.md
git -c user.name="Course Learner" -c user.email="learner@example.invalid" commit -m "Add tested unit converter"
cd ..
git clone python-starter python-starter-copy
cd python-starter-copy
python3 -m unittest -v test_app.py
```

The clone reports `done.` and the repeated test ends with `OK`.

## Add the CI Workflow

```bash
mkdir -p .github/workflows
cp ci-test.yml .github/workflows/test.yml
git add .github/workflows/test.yml
git -c user.name="Course Learner" -c user.email="learner@example.invalid" commit -m "Add CI test workflow"
```

GitHub Actions runs the same dependency, compile, and test commands after a push to a repository you control. Review the workflow before pushing. Local success does not claim a hosted CI run.

## Stage, Inject a Failure, and Keep the Prior Release

```bash
mkdir -p .stage/releases/v1
cp app.py .stage/releases/v1/app.py
ln -sfn releases/v1 .stage/current
python3 .stage/current/app.py 1
if python3 -m unittest -v test_app.py failure_fixture.py
then
  echo "UNEXPECTED DELIVERY"
else
  echo "DELIVERY BLOCKED"
fi
python3 .stage/current/app.py 1
```

The deliberate test reports one failure and prints `DELIVERY BLOCKED`. The current staged release still prints `1 meters = 3.28 feet`.

## Promote, Roll Back, and Tear Down

```bash
mkdir -p .stage/releases/v2
cp app.py .stage/releases/v2/app.py
python3 -m unittest -v test_app.py
ln -sfn releases/v2 .stage/current
python3 .stage/current/app.py 1
ln -sfn releases/v1 .stage/current
python3 .stage/current/app.py 1
rm -rf .stage
cd ..
rm -rf python-starter-copy
```

Both staged runs print `1 meters = 3.28 feet`. `test ! -e python-starter-copy/.stage` should exit successfully after teardown.

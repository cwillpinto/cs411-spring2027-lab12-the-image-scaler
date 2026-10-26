# CS411 Spring 2027 · Lab 12: The Image Scaler

Read the included handout. Complete `handle` in `handler.py`. The supplied `InMemoryStore` models an atomic conditional object write; the public tests check validation, PNG dimensions, and duplicate delivery.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python benchmark.py
```

The benchmark is a **local proxy** for FaaS timing: it measures module import once as initialization, then one first invocation and five reused-process invocations on the same source image. It is not a cloud cold-start measurement. Save its CSV output and explain that limitation in the analysis. The unchanged starter imports but fails at the intentional handler TODO.

## Work in your own GitHub repository

The instructor starter is an upstream source. Keep your completed work in a repository under your own GitHub account, then submit the repository URL and the evidence listed in the assignment handout through Blackboard.

If Blackboard links a template repository, choose **Use this template**, create the new repository under your account, and clone that new repository. Check `git remote -v` before pushing; `origin` must be your repository.

For a direct clone, first create an empty repository under your account. Replace the placeholders below with the starter link supplied in Blackboard and your own empty repository URL:

```sh
git clone <instructor-starter-url>
cd <cloned-directory>
git remote rename origin upstream
git remote add origin <your-empty-repository-url>
git remote -v
git push -u origin HEAD
```

Commit and push your completed work to your own `origin`. Do not push to the instructor's upstream repository. Use the exact submission files and verification commands in the assignment handout.

# Python for Climate Science · Workshop container

This folder runs everything you need for the workshop on your laptop, with Docker:

- **JupyterLab** to work on the notebooks of the lessons, with all Python packages installed,
- the **workshop webpage** with the lessons, the slides of each class and your *lessons learned*.

Everything you do is saved in this folder on your laptop, so nothing is lost when you stop the container.

## 1. Install Docker (once)

| System  | What to install |
|---------|-----------------|
| Windows | [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/) (accept the WSL 2 option) |
| macOS   | [Docker Desktop](https://docs.docker.com/desktop/setup/install/mac-install/) (Apple silicon or Intel) |
| Linux   | [Docker Engine](https://docs.docker.com/engine/install/) with the Compose plugin |

Start Docker Desktop (Windows, macOS) and check in a terminal that Docker works:
```
docker compose version
```

## 2. Prepare this folder (once)

Unzip the workshop file and open a terminal **in this folder** (the one with `docker-compose.yml`).
Create your `.env` file from the example and choose a password for JupyterLab:

- macOS / Linux:
  ```
  cp .env.example .env
  ```
- Windows (PowerShell):
  ```
  Copy-Item .env.example .env
  ```

Open `.env` in a text editor and replace `change-me` with your password.

**Linux only:** add your user and group id, so the files the container writes belong to you:
```
echo "UID=$(id -u)" >> .env && echo "GID=$(id -g)" >> .env
```

## 3. Start the workshop

The first time, build the container (10–15 minutes, it downloads all packages):
```
docker compose up --build
```
Every next time:
```
docker compose up
```
The first start also downloads the course into the folder `course/`. Wait until the terminal shows:
```
JupyterLab: http://localhost:8888   Webpage and slides: http://localhost:8000
```
Keep this terminal open while you work.

## 4. Open JupyterLab and the webpage

| Open in your browser    | What                                                         |
|-------------------------|--------------------------------------------------------------|
| http://localhost:8888   | **JupyterLab**: log in with the password of your `.env` file |
| http://localhost:8000   | **Webpage**: lessons, slides (*Slides* in the top bar), how-tos |

## 5. Work on the notebooks

In JupyterLab you see two folders, both yours: `notebooks` and `pages`.

1. In the file browser on the left, open `notebooks` → `lessons` → the notebook of the class,
   e.g. `class01_first_steps.ipynb`. Every start of the workshop puts the notebooks of new classes there.
2. Run a cell with `Shift+Enter`; run all with *Run → Run All Cells*. The notebooks download climate data,
   so you need internet.
3. Save with `Ctrl+S` (`Cmd+S` on macOS). Your notebooks are never overwritten by new lessons.

## 6. Write your page and send it as PDF

Every class with an exercise has a page ready for you on the webpage: *Example Student*, which you change into yours.

1. In the JupyterLab file browser, open `pages` → the folder of the class → `my_page.rst`
   (class 01: `pages/01_setup/my_page.rst`).
2. Replace the example title, name and text with yours, and save. The notebook of the class saves its pictures
   next to your page.
3. Look at it on http://localhost:8000 (*Classes → your class*): the webpage updates a few seconds after you save.
   If your page has an error, the terminal of `docker compose up` shows it.
4. Print the page in the browser (`Ctrl+P` / `Cmd+P`), choose **Save as PDF**, and send the PDF to the tutor.

More details on the webpage: *Contribute → Your Page in Each Class*.

## 7. Stop the workshop

Press `Ctrl+C` in the terminal of `docker compose up`, or run in this folder:
```
docker compose down
```
Your work stays in this folder. Start again with `docker compose up`.

## Where your work is saved

| Folder on your laptop | In JupyterLab | Content                                                  |
|-----------------------|---------------|----------------------------------------------------------|
| `my_notebooks/`       | `notebooks`   | Your notebooks: the lessons in `lessons/`, homework, data |
| `my_pages/`           | `pages`       | Your pages of the webpage, one folder per class          |
| `course/`             | (not shown)   | The course: lessons, webpage, slides; you do not need to open it |

Every start downloads the new lessons into `course/` and copies the notebooks and example pages of new classes
into your folders. Your own files are never overwritten.

## Problems?

| Message or problem | What to do |
|--------------------|------------|
| `Cannot connect to the Docker daemon` | Start Docker Desktop and try again. |
| `port is already allocated` | Another program uses port 8888 or 8000 (e.g. another Jupyter). Stop it, or change the first number of the port in `docker-compose.yml`, e.g. `"127.0.0.1:8889:8888"`, and open http://localhost:8889. |
| `Permission denied` (Linux) | Set `UID` and `GID` in `.env` (step 2) and start again. |
| `WARNING: the course was not updated` | You have no internet, or a file in `course/` was changed. Your notebooks and pages are safe: delete `course/` and start again. |
| JupyterLab asks for a token | Enter the password of your `.env` file. |
| The webpage does not change | Check the terminal of `docker compose up` for errors in your page, then reload the browser. |

## For the tutor: making the zip

This folder is `workshop/` of the course repository. Commit your changes to it, then, from the root of the
repository:

```
git archive --format=zip --prefix=tuhh_python_workshop/ -o tuhh_python_workshop.zip HEAD:workshop
```

The zip has exactly the files committed in `workshop/`: no `.env` (your password), no downloaded course, no
student files. Data the students should have from the start can be added to `my_notebooks/` of the zip.
New lessons reach the students on their next start; a change of `requirements.txt` needs `docker compose up --build`.

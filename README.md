# Daily — 2026 Routine Tracker

A personal, offline-capable dashboard for tracking daily, weekly, monthly,
quarterly, and annual disciplines — with check-ins, 1–10 self-scoring, a
streak counter, and a nightly journal. Installs to your phone's home screen
like a native app. No account, no server, no ongoing cost.

Your data is saved **only on your device**, in your browser's local storage.
Nothing is sent anywhere.

---

## What's in this folder

| File | Purpose |
|---|---|
| `routine_dashboard.html` | The app itself. Everything — layout, logic, styling — lives in this one file. |
| `manifest.json` | Tells your phone this is an installable app (name, icon, colors). |
| `icon.png` | The home-screen icon. Replace this with your own photo if you like (see below). |
| `make_icon.py` | Optional helper script that crops any photo into a proper square icon. |

You need **all three** of `routine_dashboard.html`, `manifest.json`, and
`icon.png` together when you deploy — the HTML file looks for the other two
by name in the same folder.

---

## Part 1 — Put it on the web

Your phone's "Add to Home Screen" feature needs a real URL to install from —
it won't work on a file sitting in your Downloads folder. The fastest free
way to get a URL is **Netlify Drop**, which needs no account and no coding.

1. Go to **[app.netlify.com/drop](https://app.netlify.com/drop)** in your
   computer's browser.
2. Drag all three files — `routine_dashboard.html`, `manifest.json`,
   `icon.png` — into the drop zone at once.
3. Netlify uploads them and gives you a URL that looks like
   `https://random-name-123.netlify.app`.
4. Click through to that URL and confirm you land on the tracker (not a
   blank page or file listing). If it opens a folder listing instead, click
   `routine_dashboard.html` in the list, then bookmark **that exact page**.

> **Keep this URL.** It's the one you'll open on your phone and the one
> you'll bookmark. If you ever redeploy to a *different* URL, your saved
> check-ins won't follow — see [Backing up your data](#backing-up-your-data).

### Alternative: GitHub Pages

If you'd rather have a permanent, versioned home for it (and you're already
comfortable with GitHub):

1. Create a new **public** repository, e.g. `rule-of-life-tracker`.
2. Upload the three files to the repository root (Add file → Upload files).
3. Go to **Settings → Pages**.
4. Under "Build and deployment", set **Source** to `Deploy from a branch`,
   branch `main`, folder `/ (root)`. Save.
5. Wait a minute, then your app is live at:
   `https://<your-username>.github.io/rule-of-life-tracker/routine_dashboard.html`

GitHub Pages is free forever for public repos and gives you real version
history if you keep editing the tracker over time.

---

## Part 2 — Install it on your phone

Once you have a working URL, open it **in your phone's browser** (not a
file manager, not a messaging app preview).

### iPhone (Safari)

1. Open your tracker URL in Safari.
2. Tap the **Share** icon (square with an arrow) in the toolbar.
3. Scroll down and tap **Add to Home Screen**.
4. Confirm the name (defaults to "Rule of Life") and tap **Add**.

> You must use **Safari** for this — Chrome and other browsers on iOS
> can't add full-screen home-screen apps.

### Android (Chrome)

1. Open your tracker URL in Chrome.
2. Tap the **⋮** menu (top right).
3. Tap **Add to Home screen** (or **Install app**, if Chrome offers it).
4. Confirm the name and tap **Add** / **Install**.

Either way, you'll get a home-screen icon that opens full-screen, with no
browser address bar — indistinguishable from a normal app.

---

## Using your own photo as the icon

The default icon is a set of concentric rings matching the app's design.
To swap in a personal photo instead:

### Option A — quickest, no tools needed

1. Find or take a square-ish photo (a face, a symbol, whatever feels right).
2. Resize/crop it to **512×512 pixels**, square, using your phone's photo
   editor, [Squoosh.app](https://squoosh.app), or any image tool.
3. Save it as `icon.png` (same filename), replacing the existing one.
4. Re-upload all three files to Netlify Drop (or re-push to GitHub) —
   dragging the folder in again overwrites the old deployment.
5. **Delete and re-add** the home-screen icon on your phone (removing the
   old one, then Add to Home Screen again) — phones cache the icon image,
   so just replacing the file on the server usually isn't enough to update
   an icon you've already installed.

### Option B — using the included helper script

If you're comfortable with the command line and have Python installed:

```bash
pip install Pillow --break-system-packages
python3 make_icon.py /path/to/your/photo.jpg
```

This crops your photo to a centered square with soft rounded corners and
saves it as `icon.png`, ready to redeploy. Then follow steps 4–5 above.

---

## Backing up your data

Your check-ins, scores, and journal entries are stored in your phone
browser's **local storage**, tied to the exact URL you installed from.
This means:

- Clearing Safari/Chrome site data for that URL will erase your progress.
- Reinstalling from a *different* URL starts you fresh — it won't see data
  saved under the old URL.
- There's no cloud sync between devices; each device keeps its own data.

The app includes **Export data** and **Import data** buttons in the footer
to handle exactly this:

- **Export data** downloads a JSON file (`daily-tracker-backup-YYYY-MM-DD.json`)
  containing every check-in, score, and journal entry. Save it anywhere —
  email it to yourself, drop it in cloud storage, whatever's convenient.
- **Import data** loads a previously exported file back in. You'll be asked
  whether to **merge** it with what's already on the device (imported data
  wins on conflicts, nothing else is touched) or **replace** everything
  outright.

A sensible habit: export every so often, and definitely right before you
redeploy to a new URL or set up the app on a second device — then import
that file on the new install to carry your history over.

---

## Updating the tracker later

If you add or change items again (new habits, new programs, edited
timelines), you'll get an updated `routine_dashboard.html`. To deploy the
update:

- **Netlify Drop**: drag the new files into
  [app.netlify.com/drop](https://app.netlify.com/drop) again — this
  creates a *new* URL by default, so if you want to keep the same URL,
  claim your site with a free Netlify account first (via "Team sites" after
  your first drop) so future drops update it in place instead of creating a
  new one.
- **GitHub Pages**: upload the new file(s) to the same repository — the
  live URL stays the same automatically.

Because your data lives in local storage under the URL, keeping the same
URL across updates is what keeps your history intact.

---

## Troubleshooting

| Problem | Likely cause |
|---|---|
| Icon looks blurry or stretched | Source image wasn't square, or was smaller than 512×512 |
| Home screen icon didn't update after swapping the file | Remove the installed icon and re-add it — phones cache icons |
| "Add to Home Screen" isn't full-screen / shows browser bar | On iPhone, you opened it in a non-Safari browser |
| My check-ins disappeared | You're opening a different URL than before, or the browser's site data was cleared |
| Page shows a file listing instead of the app | Link directly to `routine_dashboard.html` in that folder, and bookmark that exact link |

## **Mage → Outer Repo Workflow Cheat Sheet**

### **1️⃣ Develop in Mage**

* Use Mage UI to create pipelines, orchestrations, etc.
* Push changes in Mage UI → `mage_branch`.
* Leave `main` untouched during development.

---

### **2️⃣ Clone Mage branch temporarily**

```bash
# Outside your main repo, in a temp folder
git clone -b mage_branch git@github.com:your-user/your-repo.git temp_mage
cd temp_mage
```

* This gives you the Mage branch locally without touching your outer repo.
* ✅ Important: do NOT clone into your outer repo’s `mage/` folder.

---

### **3️⃣ Move Mage files into `mage/` folder in your outer repo**

```bash
# Create mage/ folder in your outer repo if it doesn't exist
mkdir -p ../your_outer_repo/mage

# Copy Mage code
cp -r * ../your_outer_repo/mage/

# Go back to outer repo
cd ../your_outer_repo
```

* Now your `mage/` folder contains the latest Mage pipelines.

---

### **4️⃣ Commit and push from outer repo**

```bash
git checkout main  # Make sure you’re on main branch
git add mage/
git commit -m "Update Mage pipelines in mage/ folder"
git push origin main
```

* Outer repo `main` is updated safely.
* No nested `.git` directories — Git stays clean.

---

### **5️⃣ Optional: Clean up temp folder**

```bash
rm -rf ../temp_mage
```

* Keeps your workspace tidy.

---

### **6️⃣ Key Notes / Tips**

1. **Keep Mage branch for experiments** → never merge Mage branch directly into main.
2. **Always move/copy files into `mage/` folder** before committing to main.
3. **Ignore Mage’s `.git` folder** in your outer repo `.gitignore`:

```
/mage/.git
/mage/__pycache__/
```

4. **Folder can be named anything** (`mage/`, `pipelines/`, etc.), just be consistent.
5. Repeat steps 1–5 every time you want to update Mage pipelines in main.

---

✅ **TL;DR**:

> Mage UI → Mage branch → clone temp → copy files into `mage/` folder → commit and push from main → outer repo stays clean.

---

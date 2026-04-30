<div align="center">

# ✨ NeetCode Submissions
### <a href="https://github.com/AyushSingh360">@AyushSingh360</a>

<p>
  A clean, visual, and structured archive of coding problem solutions synced from
  <a href="https://neetcode.io">NeetCode.io</a>.
</p>

<p>
  <img src="https://img.shields.io/badge/Platform-NeetCode-111827?style=for-the-badge&logo=codeforces&logoColor=white" />
  <img src="https://img.shields.io/badge/Repo-neetcode--submissions-2563eb?style=for-the-badge&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/Sync-Automatic-16a34a?style=for-the-badge&logo=githubactions&logoColor=white" />
</p>

</div>

---

## Overview

This repository stores problem submissions synced from [NeetCode.io](https://neetcode.io/).  
Every submission can be automatically pushed here, making the repo a living tracker of progress, practice, and consistency.

---

## Visual Workflow

```mermaid
flowchart TD
    A[Solve problem on NeetCode] --> B[Submit solution]
    B --> C[GitHub Sync triggers]
    C --> D[Commit pushed to repository]
    D --> E[Organized by topic]
    E --> F[Stored by problem ID]
    F --> G[Versioned as submission-0 / submission-1 / ...]
```

---

## Sync Flow

```mermaid
flowchart LR
    A[Connect GitHub account] --> B[Enable GitHub Sync]
    B --> C[Submit on NeetCode]
    C --> D[Auto push to this repo]
    B --> E[Bulk Sync old submissions]
    B --> F[Manual sync from problem history]
```

---

## Repository Structure

Solutions are organized by **topic** and then by **problem slug / ID**.  
Each attempt is stored separately so progress stays versioned and easy to review.

```bash
<topic-folder>/
└── <problem-id>/
    ├── submission-0.<ext>
    ├── submission-1.<ext>
    └── ...
```

### Example

```bash
Data Structures & Algorithms/two-integer-sum/submission-0.py
Data Structures & Algorithms/binary-search/submission-0.ts
Python For Beginners/python-hello-world/submission-0.py
```

---

## GitHub Sync Process

1. Connect your GitHub account at [neetcode.io/profile/github](https://neetcode.io/profile/github)
2. Enable sync preferences for submissions
3. Submit solutions on NeetCode
4. Let the platform auto-commit them into this repository
5. Use bulk sync to backfill older submissions
6. Use manual sync from problem history when needed

---

## Progress Snapshot

> You can update these values manually later for a more personalized dashboard.

```mermaid
pie title Progress Snapshot
    "Solved Problems" : 60
    "In Progress" : 25
    "To Revisit" : 15
```

---

## Practice Journey

```mermaid
flowchart TD
    A[Start Practice] --> B[Pick Topic]
    B --> C[Solve Problem]
    C --> D[Submit Solution]
    D --> E[Review Mistakes]
    E --> F[Retry Harder Problems]
    F --> G[Track Growth]
```

---

## Supported Languages

| Language | Extension |
|---|---|
| Python | `.py` |
| JavaScript | `.js` |
| TypeScript | `.ts` |
| Java | `.java` |
| C++ | `.cpp` |
| C# | `.cs` |

---

## Why This Repo Exists

- Track coding interview preparation in one place
- Maintain a versioned history of submissions
- Review topic-wise progress over time
- Build a public proof-of-work portfolio
- Keep solutions organized and searchable

---

## Highlights

- Automatic GitHub sync from NeetCode
- Clean topic-wise folder organization
- Separate files for multiple submissions
- Easy review of older attempts
- Great for consistency tracking and interview prep

---

## Suggested Folder Experience

For an even cleaner repo, you can gradually add:

- Topic badges in folder READMEs
- Difficulty tags for problems
- A solved-count tracker
- Language usage stats
- Monthly progress graphs

---

## Tech Stack

<p>
  <img src="https://skillicons.dev/icons?i=python,js,ts,java,cpp,cs,git,github" />
</p>

---

## Profile Note

This repository reflects ongoing problem-solving practice through NeetCode’s sync system.  
It functions as both a submission archive and a visual journey of growth in data structures, algorithms, and interview preparation.

---

<div align="center">

### ⭐ Keep building. Keep solving. Keep shipping.

</div>

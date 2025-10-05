### 🔹 **Configurazione iniziale**

| Comando                                            | Descrizione                          | Esempio                                                |
| -------------------------------------------------- | ------------------------------------ | ------------------------------------------------------ |
| `git --version`                                  | Mostra la versione di Git installata | `git --version`                                      |
| `git config --global user.name "Tuo Nome"`       | Imposta il nome utente globale       | `git config --global user.name "Mario Rossi"`        |
| `git config --global user.email "tua@email.com"` | Imposta l’email globale             | `git config --global user.email "mario@esempio.com"` |
| `git config --list`                              | Mostra la configurazione corrente    | `git config --list`                                  |

---

### 🔹 **Creazione e clonazione repository**

| Comando           | Descrizione                                             | Esempio                                              |
| ----------------- | ------------------------------------------------------- | ---------------------------------------------------- |
| `git init`      | Inizializza un nuovo repository nella cartella corrente | `git init`                                         |
| `git clone URL` | Clona un repository remoto sul computer                 | `git clone https://github.com/utente/progetto.git` |

---

### 🔹 **Gestione file**

| Comando                | Descrizione                                        | Esempio               |
| ---------------------- | -------------------------------------------------- | --------------------- |
| `git status`         | Mostra i file modificati e lo stato del repository | `git status`        |
| `git add nomefile`   | Aggiunge un file al commit                         | `git add main.py`   |
| `git add .`          | Aggiunge**tutti**i file modificati           | `git add .`         |
| `git reset nomefile` | Rimuove un file dallo stage (prima del commit)     | `git reset main.py` |

---

### 🔹 **Commit (salvataggio delle modifiche)**

| Comando                       | Descrizione                              | Esempio                                   |
| ----------------------------- | ---------------------------------------- | ----------------------------------------- |
| `git commit -m "messaggio"` | Crea un commit con messaggio descrittivo | `git commit -m "Aggiunto modulo login"` |
| `git log`                   | Mostra la cronologia dei commit          | `git log`                               |
| `git show <id_commit>`      | Mostra i dettagli di un commit specifico | `git show a1b2c3`                       |

---

### 🔹 **Branch e versioni**

| Comando                       | Descrizione                          | Esempio                   |
| ----------------------------- | ------------------------------------ | ------------------------- |
| `git branch`                | Mostra i branch locali               | `git branch`            |
| `git branch nome_branch`    | Crea un nuovo branch                 | `git branch sviluppo`   |
| `git checkout nome_branch`  | Passa a un branch diverso            | `git checkout sviluppo` |
| `git merge nome_branch`     | Unisce un branch nel branch corrente | `git merge sviluppo`    |
| `git branch -d nome_branch` | Elimina un branch locale             | `git branch -d fix-bug` |

---

### 🔹 **Interazione con repository remoto**

| Comando           | Descrizione                                | Esempio                                              |
| ----------------- | ------------------------------------------ | ---------------------------------------------------- |
| `git remote -v` | Mostra i repository remoti collegati       | `git remote -v`                                    |
| `git push`      | Invia i commit locali al repository remoto | `git push`                                         |
| `git pull`      | Scarica e unisce le modifiche dal remoto   | `git pull`                                         |
| `git fetch`     | Scarica le modifiche**senza**unirle  | `git fetch`                                        |
| `git clone`     | Clona un repository remoto                 | `git clone https://github.com/utente/progetto.git` |

---

### 🔹 **Annullare modifiche**

| Comando                      | Descrizione                                           | Esempio                     |
| ---------------------------- | ----------------------------------------------------- | --------------------------- |
| `git checkout -- nomefile` | Ripristina un file modificato all’ultimo commit      | `git checkout -- main.py` |
| `git revert <id_commit>`   | Annulla un commit creando un nuovo commit “inverso” | `git revert a1b2c3`       |
| `git reset --hard HEAD~1`  | Rimuove l’ultimo commit (⚠️ distruttivo)           | `git reset --hard HEAD~1` |

---

### 🔹 **Comandi utili per il corso**

| Comando           | Descrizione                                       | Esempio           |
| ----------------- | ------------------------------------------------- | ----------------- |
| `git diff`      | Mostra le differenze tra file modificati          | `git diff`      |
| `git stash`     | Salva modifiche temporaneamente senza fare commit | `git stash`     |
| `git stash pop` | Ripristina modifiche salvate con `stash`        | `git stash pop` |
| `git restore .` | Ripristina tutti i file non ancora committati     | `git restore .` |

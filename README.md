# 🧮 Django Pricing Manager

Une mini-application Django permettant de **gérer les produits et leurs prix**, avec calcul automatique de la **marge bénéficiaire**.  
Ce projet illustre la maîtrise de Django, du CRUD, des templates et du workflow Git.

---

## 🚀 Fonctionnalités

- ✅ CRUD complet sur les produits (ajout, modification, suppression)
- 💰 Calcul automatique de la marge (prix de vente - prix d'achat)
- 🖥️ Interface claire et moderne avec **Bootstrap**
- 🧭 Architecture Django MVC propre et documentée
- 📂 Versionnée avec Git et hébergée sur GitHub

---

## 🧩 Stack technique

| Technologie             | Utilisation                |
| ----------------------- | -------------------------- |
| **Python 3.12**         | Langage principal          |
| **Django 5.2.7**        | Framework web              |
| **SQLite (par défaut)** | Base de données            |
| **Bootstrap 5**         | Interface utilisateur      |
| **Git / GitHub**        | Versionnage et publication |

---

## ⚙️ Installation locale

```bash
# 1️⃣ Cloner le projet
git clone https://github.com/DanielEmirah/gestion_prix_django.git
cd gestion_prix_django

# 2️⃣ Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows

# 3️⃣ Installer les dépendances
pip install -r requirements.txt

# 4️⃣ Appliquer les migrations
python manage.py migrate

# 5️⃣ Lancer le serveur
python manage.py runserver
```

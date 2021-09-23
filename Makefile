runserver:
	@echo "🚀 Go to the moon"
	python3 manage.py runserver

apply_migrations:
	@echo "👨‍🔧 Applying migrations"
	python3 manage.py makemigrations
	python3 manage.py migrate

	@echo "✅ All done"

reset_database:
	@echo "🗑 Clearing existing data"
	python3 manage.py flush --noinput

	@echo "👨‍🔧 Applying migrations"
	python3 manage.py makemigrations
	python3 manage.py migrate

	@echo "✅ All done"

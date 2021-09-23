runserver:
	@echo "🚀 Go to the moon"
	python3 manage.py runserver

apply_migrations:
	@echo "👨‍🔧 Applying migrations"
	python3 manage.py makemigrations

	@echo "👨‍🔧 Applying Database"
	python3 manage.py migrate

	@echo "✅ All done"

reset_data:
	@echo "👨‍🔧 Clearing all tables and create new Database"
	python3 manage.py flush --noinput

	@echo "✅ All done"

clear_database:
	@echo "👨‍🔧 Dropping  all tables"
	python3 manage.py reset_db --noinput

	@echo "✅ All done"

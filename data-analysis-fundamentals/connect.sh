# Principle: don't do work
source .env
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USERNAME -p $DB_PORT -d $DB_NAME
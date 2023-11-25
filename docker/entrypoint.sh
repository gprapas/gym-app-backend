#!/bin/sh

# Wait until the DB container is ready to accept connections
while ! nc -z $DB_DEFAULT_HOST $DB_DEFAULT_PORT ; do
    echo "Waiting for the DB Instance"
    sleep 3
done


# Do the migrations first
python manage.py makemigrations
python manage.py migrate

#(Optional) the fixtures to populate db.
fixtures=${FIXTURES:-false}
if [ "$fixtures" = "true" ]; then
    echo  "|==================================================|"
    echo  "|          Populate database with data...          |"
    echo  "|==================================================|"
    for py_file in $(find fixtures -name "*.json")
    do
        python manage.py loaddata $py_file
    done
    echo  "|==================================================|"
    echo  "|         All Fixtures loaded successfully.        |"
    echo  "|==================================================|"
else 
    echo  "|==================================================|"
    echo  "|               No fixtures loaded.                |"
    echo  "|==================================================|"
fi

# the app
echo "|==================================================|"
echo "|   Your app is running at 0.0.0.0:8000            |"
echo "|==================================================|"
python manage.py runserver 0.0.0.0:8000

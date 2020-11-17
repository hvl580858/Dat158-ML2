import psycopg2


def execute_sql(sql, params):
    try:
        connection = psycopg2.connect(
            user="abjaykmgqyrfmn",
            password="fe036509d198e4b10c24c1a50c576867af01b19afa3ff2f0a1f9edfba6eda8d8",
            host="ec2-34-254-24-116.eu-west-1.compute.amazonaws.com",
            port="5432",
            database="d405qjg06557ab"
        )
        cursor = connection.cursor()
        cursor.execute(sql, params)
        pred = cursor.fetchall()

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close

    return pred
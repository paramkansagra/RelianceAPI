from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from dateutil import parser
from datetime import datetime
from django.db import connection


class dev(ViewSet):
    @action(methods=["POST"], detail=False)
    def import_data(self, request):
        def getDateTime(system_time):
            try:
                date = parser.parse(system_time)
                _when = date.strftime("%Y-%m-%d %H:%M:%S%z")
                aha = _when[-1:-5:-1]
                _when = _when[:-4]

                newFormat = aha[:2] + ":" + aha[2:]

                _when += newFormat
                return _when
            except:
                return ""

        def createQuery(data, tableName):
            columnNames = ",".join(data.keys())
            valueData = []
            for i in data:
                if type(data[i]) == int:
                    valueData.append(str(data[i]))
                else:
                    # lets check for date
                    if getDateTime(data[i]) != "":
                        string = "'" + getDateTime(data[i]) + "'"
                        valueData.append(string)
                    else:
                        string = "'" + data[i] + "'"
                        valueData.append(string)

            values = ",".join(valueData)

            query = "insert into {0} ({1}) values({2});".format(
                table_name[0], columnNames, values
            )
            cursor.execute(query)

        data = request.data
        cursor = connection.cursor()

        cursor.execute("SHOW TABLES")
        table_names = cursor.fetchall()

        table_name = (data["Table Name"],)
        if table_name in table_names:
            requestData = data["data"]
            for i in requestData:
                createQuery(i, table_name)
        else:
            print("table not in db")

        return Response("All OK", status=200)

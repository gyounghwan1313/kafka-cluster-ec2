
import requests as req
import json


s3_sink_connector ={"name":"subway-arrival-s3-sink",
                    "config": {"connector.class":"io.confluent.connect.s3.S3SinkConnector",
                                "tasks.max":1,
                                "topics":"subway-arrival-topic",
                                "s3.region":"ap-northeast-2",
                                "s3.bucket.name":"subway-arrival",
                                "s3.compression.type":"gzip",
                                "s3.part.size":5242880,
                                "flush.size":1,
                                "storage.class":"io.confluent.connect.s3.storage.S3Storage",
                                "format.class":"io.confluent.connect.s3.format.json.JsonFormat",
                                "schema.generator.class":"io.confluent.connect.storage.hive.schema.DefaultSchemaGenerator",
                                "partitioner.class":"io.confluent.connect.storage.partitioner.TimeBasedPartitioner",
                                "partition.duration.ms":3600000,
                                "path.format":"YYYY-MM-dd",
                                "locale":"KR",
                                "timezone":"Asia/Seoul",
                                "schema.compatibility":"NONE"
                               }
                    }



result = req.post(url="http://ec2-52-78-111-200.ap-northeast-2.compute.amazonaws.com:8083/connectors",headers={"Content-Type": "application/json"},data=json.dumps(s3_sink_connector))
print(result.json())
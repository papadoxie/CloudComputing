#!/usr/bin/env bash
HADOOP_HOME=/home/papadoxie/Code/CloudComputing/Hadoop/hadoop-3.3.6

rm -rf output
$HADOOP_HOME/bin/hdfs dfs -rm -r input
$HADOOP_HOME/bin/hdfs dfs -rm -r output

$HADOOP_HOME/bin/hdfs dfs -mkdir input
$HADOOP_HOME/bin/hdfs dfs -put input/* input

$HADOOP_HOME/bin/hadoop jar ../../hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
    -files mapper.py,reducer.py,input/negative_words.txt,input/positive_words.txt,input/stop_words.txt \
    -mapper mapper.py \
    -reducer reducer.py \
    -input input/twitter.json \
    -output output

$HADOOP_HOME/bin/hdfs dfs -get output output
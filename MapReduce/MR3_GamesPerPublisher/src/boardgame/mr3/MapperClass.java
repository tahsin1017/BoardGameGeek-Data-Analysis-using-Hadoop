package boardgame.mr3;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MapperClass
        extends Mapper<LongWritable, Text, Text, IntWritable> {

    private static final IntWritable ONE = new IntWritable(1);

    @Override
    protected void map(
            LongWritable key,
            Text value,
            Context context
    ) throws IOException, InterruptedException {

        String line = value.toString().trim();

        if (line.isEmpty()) {
            return;
        }

        String[] fields = line.split(",", -1);

        if (fields.length != 13) {
            return;
        }

        String publisher = fields[3].trim();

        if (publisher.isEmpty()) {
            return;
        }

        context.write(
                new Text(publisher),
                ONE
        );
    }
}

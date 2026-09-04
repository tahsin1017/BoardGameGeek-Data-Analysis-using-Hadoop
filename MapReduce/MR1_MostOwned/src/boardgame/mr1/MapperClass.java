package boardgame.mr1;

import java.io.IOException;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MapperClass extends Mapper<LongWritable, Text, Text, Text> {

    private static final Text OUT_KEY = new Text("max");

    @Override
    protected void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {

        String line = value.toString().trim();

        if (line.isEmpty()) {
            return;
        }

        String[] fields = line.split(",", -1);

        if (fields.length != 13) {
            return;
        }

        String gameID = fields[0];
        String name = fields[1];
        String owned = fields[10];

        try {
            long ownedCount = Long.parseLong(owned);

            context.write(
                OUT_KEY,
                new Text(gameID + "\t" + name + "\t" + ownedCount)
            );

        } catch (NumberFormatException e) {
            // Ignore malformed numeric records
        }
    }
}

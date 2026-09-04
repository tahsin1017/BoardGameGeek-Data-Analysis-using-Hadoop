package boardgame.mr1;

import java.io.IOException;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class ReducerClass extends Reducer<Text, Text, Text, Text> {

    @Override
    protected void reduce(Text key, Iterable<Text> values, Context context)
            throws IOException, InterruptedException {

        long maxOwned = -1;
        String maxGameID = "";
        String maxName = "";

        for (Text value : values) {

            String[] parts = value.toString().split("\t", -1);

            if (parts.length != 3) {
                continue;
            }

            try {
                long owned = Long.parseLong(parts[2]);

                if (owned > maxOwned) {
                    maxOwned = owned;
                    maxGameID = parts[0];
                    maxName = parts[1];
                }

            } catch (NumberFormatException e) {
                // Ignore malformed values
            }
        }

        if (maxOwned >= 0) {
            context.write(
                new Text(maxGameID),
                new Text(maxName + "\t" + maxOwned)
            );
        }
    }
}

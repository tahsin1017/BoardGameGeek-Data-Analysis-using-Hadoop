package boardgame.mr2;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MapperClass
        extends Mapper<LongWritable, Text, Text, Text> {

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

        String gameID = fields[0];
        String usersRated = fields[8];
        String averageRating = fields[9];
        String numComments = fields[11];

        try {
            long ratedCount = Long.parseLong(usersRated);
            double avgRating = Double.parseDouble(averageRating);
            long comments = Long.parseLong(numComments);

            String outValue =
                    avgRating + "\t" +
                    ratedCount + "\t" +
                    comments;

            context.write(
                    new Text(gameID),
                    new Text(outValue)
            );

        } catch (NumberFormatException e) {
            // Ignore malformed numeric records
        }
    }
}

import twitter4j.*;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class TwitterTry {
    /**
     * Usage: java twitter4j.examples.search.SearchTweets [query]
     *
     * @param args search query
     */
	
	private static ArrayList<TweetPack> returnList = new ArrayList<TweetPack>();
	private static File file = null;
	private static String fileName = "twitter.csv";
	
	static class TweetPack{
		private String name;
		private String content;
		private int friendCount;
		private Date date;
		
		public TweetPack(String name, String content, int friendCount, Date date){
			this.name = name;
			this.content = content;
			this.friendCount = friendCount;
			this.date = date;
		}
		
		public String getName() { return name;}
		public String getContent() { return content;}
		public int getFriendCount() { return friendCount;}
		public String getDate() { 
			DateFormat df = new SimpleDateFormat("MM/dd/yyyy HH:mm:ss");
			String dateS = df.format(date);
			return dateS;
		}
	}
	
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("java twitter4j.examples.search.SearchTweets [query]");
            System.exit(-1);
        }
        
        Twitter twitter = new TwitterFactory().getInstance();
        try {
            Query query = new Query(args[0]).since("2013-3-30");
            QueryResult result;
            int count = 0;
            do {
                result = twitter.search(query);
                List<Status> tweets = result.getTweets();
                for (Status tweet : tweets) {
                	String name = tweet.getUser().getScreenName();
                	String content = tweet.getText();
                	Date createDate = tweet.getCreatedAt();
                	int number = tweet.getUser().getFriendsCount();
                    //System.out.println("@" + tweet.getUser().getScreenName() + " - " + tweet.getText());
                    returnList.add(new TweetPack(name,content,number,createDate));
                    //System.out.println("The friend count is "+tweet.getUser().getFriendsCount());
                }
                count++;
            } while (((query = result.nextQuery()) != null)&&(count < 100));
            System.out.println("The number of records is "+Integer.toString(returnList.size()));
        } catch (TwitterException te) {
            te.printStackTrace();
            System.out.println("Failed to search tweets: " + te.getMessage());
            System.exit(-1);
        }
        
        try{
        	file = new File(fileName);
        	for(int i=0;i<returnList.size();i++){
        		writeToFile(returnList.get(i));
        	}
        }
        catch (Exception e){
        	e.printStackTrace();
        }
        
        System.exit(0);
    }
    
    public static void writeToFile(TweetPack pack){
    	BufferedWriter writer;
    	try{
    		writer = new BufferedWriter(new FileWriter(fileName,true));
    		writer.write(pack.getName()+","+pack.getContent()+","+pack.getFriendCount()+","+pack.getDate());
    		writer.newLine();
    		writer.flush();
    		writer.close();
    	} catch (Exception e){
            System.err.println("Unexpected I/O error when writing to file.");
            e.printStackTrace();
        }
    }
}
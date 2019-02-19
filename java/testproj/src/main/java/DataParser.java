import org.apache.commons.io.FileUtils;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

public class DataParser
{

    public static void main(String[] args)
    {

        try
        {
            List<String> lines = FileUtils.readLines(new File("/Users/darioflores/Documents/machineLearn/java/ml-latest-small/ratings.csv"),
                    "UTF-8");

            System.out.println("All::" + lines.size());
            lines.remove(0);
            final List<String> newlines = lines;//lines.subList(10000,20000);

            lines = null;

            final Set<String> customerSet = new HashSet<String>();
            final Set<String> productSet = new HashSet<String>();

            Map<String, Map<String, String>> userReviews = new HashMap<String, Map<String, String>>();

            Map<String, Integer> custReviewsCount = new HashMap<String, Integer>();
            Map<String, Integer> prodReviewsCount = new HashMap<String, Integer>();

            //customer_id,product_id,star_rating,verified_purchase

            newlines.stream()
                    .map(line -> line.split(","))
                    .forEach(line -> {

                        final String customer = line[0].toLowerCase().trim();
                        final String product = line[1].toLowerCase().trim();
                        final String rating = line[2].toLowerCase().trim();

                        customerSet.add(customer);
                        productSet.add(product);

                        if (custReviewsCount.containsKey(customer))
                        {

                            custReviewsCount.put(customer, custReviewsCount.get(customer) + 1);

                        }
                        else
                        {
                            custReviewsCount.put(customer, 1);
                        }

                        //
                        if (prodReviewsCount.containsKey(product))
                        {

                            prodReviewsCount.put(product, prodReviewsCount.get(product) + 1);

                        }
                        else
                        {
                            prodReviewsCount.put(product, 1);
                        }

                        Map<String, String> productsMap = null;

                        if (userReviews.containsKey(customer))
                        {
                            productsMap = userReviews.get(customer);
                        }
                        else
                        {

                            productsMap = new HashMap<String, String>();
                            userReviews.put(customer, productsMap);

                        }

                        productsMap.put(product, rating);

                        //System.out.println(customer+","+product+","+rating );
                    });

            System.out.println("customerSet::" + customerSet.size());
            System.out.println("-productSet::" + productSet.size());

            final ArrayList<String> customerList = new ArrayList<String>(customerSet);

            final List<String> productList = (new ArrayList<String>(productSet)).stream()
                    .filter(prod -> prodReviewsCount.get(prod) >= 35)
                    .collect(Collectors.toList());

            final ArrayList<String> finalLines = new ArrayList<String>();

            final String idNameMap = getProductIdNameMap(productList);
            finalLines.add("custid,"+idNameMap);

            for (final String cust : customerList)
            {

                final StringBuffer sb = new StringBuffer();

                sb.append(cust);

                final Map<String, String> reviews = userReviews.get(cust);

                if (reviews != null && reviews.size() > 0)
                {

                    for (final String prod : productList)
                    {

                        if (reviews.containsKey(prod))
                        {
                            sb.append("," + reviews.get(prod));
                        }
                        else
                        {
                            sb.append(",");
                        }
                    }

                    //System.out.println(sb.toString());
                    finalLines.add(sb.toString());

                }

            }//

            FileUtils.writeLines(new File("/Users/darioflores/Documents/machineLearn/java/testproj/reviewsTable_0_30.csv"), finalLines);

        }
        catch (IOException e)
        {
            e.printStackTrace();
        }

    }

    public static String getProductIdNameMap(final List<String> productList)
    {

        try
        {
            List<String> lines = FileUtils.readLines(new File("/Users/darioflores/Documents/machineLearn/java/ml-latest-small/movies.csv"),
                    "UTF-8");

            final Map<String, String> idNamesMap = new HashMap<String, String>();

            for (String line : lines)
            {

                if (line != null && !line.isEmpty())
                {

                    final String[] split = line.split(",");

                    final String id = split[0];
                    final String ll = split[split.length - 1];
                    final String name = line.replace(id, "").replace(ll, "")
                            .trim()
                            .replaceAll("^,", "")
                            .replaceAll(",$", "")
                            .replace("\"","")
                            .replace(","," ")
                            .replace("  "," ")
                            .trim();

                    idNamesMap.put(id, name);
                }
            }

            final String collect = productList.stream()
                    .map(code -> idNamesMap.get(code))
                    .collect(Collectors.joining(","));

            System.out.println(collect);
            return collect;

        }
        catch (IOException e)
        {
            e.printStackTrace();
        }

        return "";

    }

}

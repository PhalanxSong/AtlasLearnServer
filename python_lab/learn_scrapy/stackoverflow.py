import scrapy
class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    start_urls = ['http://stackoverflow.com/questions?sort=votes']
    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)
    def parse_question(self, response):
        yield {
            'title': response.css('h1 a::text').extract()[0],
            'votes': response.css('.question .vote-count-post::text').extract()[0],
            'body': response.css('.question .post-text').extract()[0],
            'tags': response.css('.question .post-tag::text').extract(),
            'link': response.url,
        }


    # {
    #     "title": "Why is it faster to process a sorted array than an unsorted array?",
    #     "votes": "18692",
    #     "body": "<div class=\"post-text\" itemprop=\"text\">\r\n\r\n<p>Here is a piece of C++ code that seems very peculiar. For some strange reason, sorting the data miraculously makes the code almost six times faster.</p>\n\n<pre class=\"lang-cpp prettyprint-override\"><code>#include &lt;algorithm&gt;\n#include &lt;ctime&gt;\n#include &lt;iostream&gt;\n\nint main()\n{\n    // Generate data\n    const unsigned arraySize = 32768;\n    int data[arraySize];\n\n    for (unsigned c = 0; c &lt; arraySize; ++c)\n        data[c] = std::rand() % 256;\n\n    // !!! With this, the next loop runs faster\n    std::sort(data, data + arraySize);\n\n    // Test\n    clock_t start = clock();\n    long long sum = 0;\n\n    for (unsigned i = 0; i &lt; 100000; ++i)\n    {\n        // Primary loop\n        for (unsigned c = 0; c &lt; arraySize; ++c)\n        {\n            if (data[c] &gt;= 128)\n                sum += data[c];\n        }\n    }\n\n    double elapsedTime = static_cast&lt;double&gt;(clock() - start) / CLOCKS_PER_SEC;\n\n    std::cout &lt;&lt; elapsedTime &lt;&lt; std::endl;\n    std::cout &lt;&lt; \"sum = \" &lt;&lt; sum &lt;&lt; std::endl;\n}\n</code></pre>\n\n<ul>\n<li>Without <code>std::sort(data, data + arraySize);</code>, the code runs in 11.54 seconds.</li>\n<li>With the sorted data, the code runs in 1.93 seconds.</li>\n</ul>\n\n<p>Initially, I thought this might be just a language or compiler anomaly. So I tried it in Java.</p>\n\n<pre class=\"lang-java prettyprint-override\"><code>import java.util.Arrays;\nimport java.util.Random;\n\npublic class Main\n{\n    public static void main(String[] args)\n    {\n        // Generate data\n        int arraySize = 32768;\n        int data[] = new int[arraySize];\n\n        Random rnd = new Random(0);\n        for (int c = 0; c &lt; arraySize; ++c)\n            data[c] = rnd.nextInt() % 256;\n\n        // !!! With this, the next loop runs faster\n        Arrays.sort(data);\n\n        // Test\n        long start = System.nanoTime();\n        long sum = 0;\n\n        for (int i = 0; i &lt; 100000; ++i)\n        {\n            // Primary loop\n            for (int c = 0; c &lt; arraySize; ++c)\n            {\n                if (data[c] &gt;= 128)\n                    sum += data[c];\n            }\n        }\n\n        System.out.println((System.nanoTime() - start) / 1000000000.0);\n        System.out.println(\"sum = \" + sum);\n    }\n}\n</code></pre>\n\n<p>With a somewhat similar but less extreme result.</p>\n\n<hr>\n\n<p>My first thought was that sorting brings the data into the cache, but then I thought how silly that is because the array was just generated.</p>\n\n<ul>\n<li>What is going on?</li>\n<li>Why is a sorted array faster to process than an unsorted array?</li>\n<li>The code is summing up some independent terms, and the order should not matter.</li>\n</ul>\n    </div>",
    #     "tags": [
    #         "java",
    #         "c++",
    #         "performance",
    #         "optimization",
    #         "branch-prediction"
    #     ],
    #     "link": "https://stackoverflow.com/questions/11227809/why-is-it-faster-to-process-a-sorted-array-than-an-unsorted-array"
    # },
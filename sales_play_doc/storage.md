Engineering our tiered storage subsystem from the ground up #
When I talk about Shadow Indexing, I’m talking about the architecture that enables cloud storage from Redpanda’s core product. Tiered storage is a feature that leverages the  Shadow Indexing architecture to offload data to the cloud, thereby helping our customers save money on storage costs. To engineer our Shadow Indexing subsystem, we started completely from scratch and built the architecture to where it is now.


Our core platform is powered by the Seastar framework, which is unique because it lets us use the full capabilities of modern hardware. To engineer tiered storage through Seastar, we had to start out building very basic features. This included building an HTTP server and S3 client. After some of the more basic components of the system were built, we moved on with the development of the tiered storage subsystem.

When the architecture was set up, we went GA with Shadow Indexing and Tiered Storage. You can read more about all of these components and how our read and write paths work in my detailed blog post about the architecture here.

As with engineering any new software, developing Shadow Indexing wasn’t without its challenges, but I think the end solution has been a good addition to the Redpanda platform. It allows infinite data retention with good performance at a low cost. Additionally, we’re always planning improvements for Redpanda, and we’ll continue engineering new features for Shadow Indexing in the future. A few items on our list right now are faster data balancing, full cluster recovery, and improved handling of analytical clusters.  

Because I like working on projects from the very start and for long periods of time, Shadow Indexing has been especially rewarding to work on. I’ve enjoyed seeing how gradual improvements accumulate and turn proof of concept into a mature product, and I’m excited to see what comes next for Shadow Indexing.

Shadow Indexing and edge computing #
I also like working on Shadow Indexing because it aligns well with my interests. I like to work on storage-related projects and I’m also interested in edge computing. Shadow Indexing includes a bit of both. It allows Redpanda to be used in remote locations with our new feature called Remote Read Replicas. In some sense, Redpanda can be used as a CDN for streaming data that allows consumers to be on the edge instead of a centralized data center.

For example, perhaps your company has a central database in one location, but it also has various servers around the world. Moving this data across geographic locations can be tricky, but read replicas allow us to store those data in the cloud and make them accessible anywhere.

Owning your work as an engineer #
This job is different from many other engineering jobs. The team here gives you lots of freedom and trust, and you have many opportunities to make an impact on the software we develop. You have a sense of ownership over the projects you work on here because your opinions are taken into account, and it's easy to feel motivated because of that.

In my experience building Shadow Indexing, I got to work on a project for the company over an extended period of time and it had a big impact on what we’re now able to offer to users. Being able to make a difference like that isn’t necessarily something that you can do in any engineering role.

We’re hiring - Check out our Careers page! #
We’re currently hiring for several teams across the company. If working here sounds interesting to you, head over to Careers and browse our open roles. In addition to making an impact on the projects you build, you’ll also get some great benefits, including unlimited vacation days.

Learn more about Redpanda by trying our free Community Edition, check out our source-available GitHub repo, or join the Redpanda Community on Slack to see what other devs are building with Redpanda.

‍
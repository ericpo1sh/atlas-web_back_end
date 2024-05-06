### Learning Objectives

### General

- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- What the purpose of a caching system
- What limits a caching system have

**Read or watch**:

[https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_(FIFO)](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_(FIFO))

### What I Learned

FIFO: 
With this algorithm, the cache behaves like a [FIFO queue](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)); it evicts blocks in the order in which they were added, regardless of how often or how many times they were accessed before.

LIFO/FILO:
The cache behaves like a [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)),
and unlike a FIFO queue. The cache evicts the block added most recently
first, regardless of how often or how many times it was accessed 
before.

**Least recently used (LRU):**

Discards least recently used items first. This algorithm requires 
keeping track of what was used and when, which is cumbersome. It 
requires "age bits" for [cache lines](https://en.wikipedia.org/wiki/CPU_cache#Cache_entries), and tracks the least recently used cache line based on them. When a cache line is used, the age of the other cache lines changes. LRU is [a family of caching algorithms](https://en.wikipedia.org/wiki/Page_replacement_algorithm#Variants_on_LRU). The access sequence for the example is A B C D E D F:

!https://upload.wikimedia.org/wikipedia/commons/8/88/Lruexample.png

**Most-recently-used (MRU):** 

Unlike LRU, MRU discards the most-recently-used items first. 
(also known as cyclic access patterns), MRU cache algorithms have more 
hits than LRU due to their tendency to retain older data.[[11]](https://en.wikipedia.org/wiki/Cache_replacement_policies#cite_note-11)
MRU algorithms are most useful in situations where the older an item 
is, the more likely it is to be accessed. The access sequence for the 
example is A B C D E C D B:

!https://upload.wikimedia.org/wikipedia/commons/4/43/Mruexample.png

**Least frequently used (LFU):**

The LFU algorithm counts how often an item is needed; those used less often are discarded first. This is similar to LRU, except that how many times a block was accessed is stored instead of how recently. While running an access sequence, the block which was used the fewest times will be removed from the cache. 

## What is the purpose of a caching system?

A caching system stores frequently accessed data to improve system performance by reducing access time, relieving strain on resources, enhancing scalability, saving costs, and providing a better user experience.

## What limits a caching system have?

1. **Cache Invalidation:** Ensuring cached data stays current is a challenge.
2. **Eviction Policies:** Limited cache space requires effective strategies for removing old data.
3. **Cold Start:** Initially, caches might have no data, impacting performance.
4. **Coherency in Distributed Systems:** Maintaining consistent cache views across nodes can be complex.
5. **Storage Overhead:** Caching systems require additional resources.
6. **Security Concerns:** Malicious users can exploit caching systems.
7. **Cache Warming:** Preparing caches with initial data can be resource-intensive.

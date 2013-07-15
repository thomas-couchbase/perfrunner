from perfrunner.tests import PerfTest
from perfrunner.tests.index import IndexTest


class BucketCompactionTest(PerfTest):

    def run(self):
        self.run_load_phase()  # initial load
        self.run_load_phase()  # extra mutations for bucket fragmentation

        self.reporter.start()
        self.compact_bucket()
        value = self.reporter.finish('Bucket compaction')
        self.reporter.post_to_sf(value)


class IndexCompactionTest(IndexTest):

    def run(self):
        self.run_load_phase()

        self.define_ddocs()
        self.build_index()

        self.run_load_phase()  # extra mutations for index fragmentation
        self.build_index()

        self.reporter.start()
        self.compact_index()
        value = self.reporter.finish('Index compaction')
        self.reporter.post_to_sf(value)

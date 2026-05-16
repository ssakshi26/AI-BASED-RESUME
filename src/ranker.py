class Ranker:
    @staticmethod
    def rank_resumes(results):
        """
        Sorts the list of results by score in descending order.
        """
        return sorted(results, key=lambda x: x['score'], reverse=True)

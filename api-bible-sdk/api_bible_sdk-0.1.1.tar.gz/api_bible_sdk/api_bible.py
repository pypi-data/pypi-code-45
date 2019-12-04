import requests

import json


class APIBible:
    def __init__(self, access_token):
        """
        :param access_token: The token used to access the api.bible API
            Type = String
        """
        self.headers = {"api-key": access_token}
        self.base_url = "https://api.scripture.api.bible/"

    def get_bibles(self, language=None, abbreviation=None, name=None, ids=None):
        """
        List all avalible bibles with optional query params:
        
        :param language: (optional) ISO 639-3 three digit langage code used to filter results
            Type = String 
        :param abbreviation: (optional) Bible abbreviation to search for
            Type = String 
        :param name: (optional) Bible name to search for
            Type = String 
        :param ids: (optional) Comma separated list of Bible Ids to return
            Type = String 
        """
        querystring = {
            "language": language,
            "abbreviation": abbreviation,
            "name": name,
            "ids": ids,
        }
        response = requests.get(
            self.base_url + "v1/bibles", headers=self.headers, params=querystring
        )
        return json.loads(response.text)["data"]

    def get_bible(self, bible_id):
        """
        Retrieves a single bible matching the bible_id

        :param bible_id: Id of Bible to be fetched
            Type = String
        """
        response = requests.get(
            self.base_url + f"v1/bibles/{bible_id}", headers=self.headers
        )
        j = json.loads(response.content)["data"]
        return j

    def get_books(
        self, bible_id, include_chapters=False, include_chapters_and_sections=False
    ):
        """
        Retrieves all of the books for the bible_id

        :param bible_id: Id of the Bible to get the books from
            Type = String
        :param include_chapters: (optional) if an array of chapter summaries should be included in the results
            Type = Boolean
        :param include_chapters_and_sections: (optional) if an array of chapter summaries and an array of sections should be included in the results
            Type = Boolean
        """
        querystring = {
            "include-chapters": include_chapters,
            "include-chapters-and-sections": include_chapters_and_sections,
        }
        response = requests.get(
            self.base_url + f"v1/bibles/{bible_id}/books",
            headers=self.headers,
            params=querystring,
        )
        return json.loads(response.text)["data"]

    def get_book(self, bible_id, book_id, include_chapters=False):
        """
        Retrieves the book_id of the bible matching the bible_id

        :param bible_id: Id of the Bible to get the books from
            Type = String
        "param book_id: Id of the book to retrieve
            Type = String
        :param include_chapters: (optional) if an array of chapter summaries should be included in the results
            Type = Boolean
        """
        querystring = {"include-chapters": include_chapters}
        response = requests.get(
            self.base_url + f"v1/bibles/{bible_id}/books/{book_id}",
            headers=self.headers,
            params=querystring,
        )
        return json.loads(response.text)["data"]

    def get_chapters(self, bible_id, book_id):
        """
        Retrieves all of the chapters for the bible_id and book_id

        :param bible_id: Id of the Bible to get the chapters from
            Type = String
        : param book_id: Id of the book to get the chapters from
            Type = String
        """
        response = requests.get(
            self.base_url + f"v1/bibles/{bible_id}/books/{book_id}/chapters",
            headers=self.headers,
        )
        return json.loads(response.text)["data"]

    def get_chapter(
        self,
        bible_id,
        chapter_id,
        content_type="html",
        include_notes=False,
        include_titles=False,
        include_chapter_numbers=False,
        include_verse_numbers=False,
        include_verse_spans=False,
        parallels=None,
    ):
        """
        Gets a single Chapter object for a given bible_id and chapter_id

        :param bible_id: Id of the Bible to get the chapter from
            Type = String
        :param chapter_id: Id of the chapter to get
            Type = String
        :param content_type: (optional) Content type to be returned in the content property
            Type = String
            Supported Values = [ "html", "json", "text" ]
        :param include_notes: (optional) Include footnotes in content
            Type = Boolean
        :param include_titles: (optional) Include section titles in content
            Type = Boolean
        :param include_chapter_numbers: (optional) Include chapter numbers in content
            Type = Boolean
        :param include_verse_numbers: (optional) Include verse numbers in content
            Type = Boolean
        :param include_verse_spans: (optional) Include spans that wrap verse numbers and verse text for bible content
            Type = Boolean
        :param parallels: (optional) Comma delimited list of bible_ids to include
            Type = String
        """
        querystring = {
            "content-type": content_type,
            "include-notes": include_notes,
            "include-titles": include_titles,
            "include-chapter-numbers": include_chapter_numbers,
            "include-verse-numbers": include_verse_numbers,
            "include-verse-spans": include_verse_spans,
            "parallels": parallels,
        }
        response = requests.get(
            self.base_url + f"v1/bibles/{bible_id}/chapters/{chapter_id}",
            headers=self.headers,
            params=querystring,
        )
        return json.loads(response.text)["data"]

    def get_passages(
        self,
        bible_id,
        passage_id,
        content_type="html",
        include_notes=False,
        include_titles=False,
        include_chapter_numbers=False,
        include_verse_numbers=False,
        include_verse_spans=False,
        parallels=None,
        use_org_id=False,
    ):
        """
        Gets a Passage object for a given bible_id and passage_id

        :param bible_id: Id of the Bible to get the chapter from
            Type = String
        :param passage_id: String reference id for the requested passage
            Type = String
        :param content_type: (optional) Content type to be returned in the content property
            Type = String
            Supported Values = [ "html", "json", "text" ]
        :param include_notes: (optional) Include footnotes in content
            Type = Boolean
        :param include_titles: (optional) Include section titles in content
            Type = Boolean
        :param include_chapter_numbers: (optional) Include chapter numbers in content
            Type = Boolean
        :param include_verse_numbers: (optional) Include verse numbers in content
            Type = Boolean
        :param include_verse_spans: (optional) Include spans that wrap verse numbers and verse text for bible content
            Type = Boolean
        :param parallels: (optional) Comma delimited list of bible_ids to include
            Type = String
        :param use_org_id: (optional) Use the supplied id(s) to match the verseOrgId instead of the verseId
            Type = Boolean
        """
        querystring = {
            "content-type": content_type,
            "include-notes": include_notes,
            "include-titles": include_titles,
            "include-chapter-numbers": include_chapter_numbers,
            "include-verse-numbers": include_verse_numbers,
            "include-verse-spans": include_verse_spans,
            "parallels": parallels,
            "use-org-id": use_org_id,
        }
        response = requests.get(
            self.base_url + f"v1/bibles/{bible_id}/passages/{passage_id}",
            headers=self.headers,
            params=querystring,
        )
        return json.loads(response.text)["data"]

    def get_book_sections(self, bible_id, book_id):
        """
        Gets an array of Section objects for a given bible_id and book_id

        :param bible_id: Id of Bible whose Sections to fetch
            Type = String
        "param book_id: Id of the Book whose Sections to fetch
            Type = String
        """
        response = requests.get(
            self.base_url + f"v1/bibles/{bible_id}/books/{book_id}/sections",
            headers=self.headers,
        )
        return json.loads(response.text)["data"]

    def get_chapter_sections(self, bible_id, chapter_id):
        """
        Gets an array of Section objects for a given bible_id and chapter_id


        :param bible_id: Id of the Bible to get the chapter from
            Type = String
        :param chapter_id: Id of the chapter to get
            Type = String
        """
        response = requests.get(
            self.base_url + f"v1/bibles/{bible_id}/chapters/{chapter_id}/sections",
            headers=self.headers,
        )
        return json.loads(response.text)["data"]

    def get_section(
        self,
        bible_id,
        section_id,
        content_type="html",
        include_notes=False,
        include_titles=False,
        include_chapter_numbers=False,
        include_verse_numbers=False,
        include_verse_spans=False,
        parallels=None,
    ):
        """
        Gets a single Section object for a given bible_id and section_id.
        This Section object also includes an content property with all verses for the Section.

        :param bible_id: Id of Bible whose Section to fetch
            Type = String
        :param section_id: Id of the Section to fetch
            Type = String
        :param content_type: (optional) Content type to be returned in the content property
            Type = String
            Supported Values = [ "html", "json", "text" ]
        :param include_notes: (optional) Include footnotes in content
            Type = Boolean
        :param include_titles: (optional) Include section titles in content
            Type = Boolean
        :param include_chapter_numbers: (optional) Include chapter numbers in content
            Type = Boolean
        :param include_verse_numbers: (optional) Include verse numbers in content
            Type = Boolean
        :param include_verse_spans: (optional) Include spans that wrap verse numbers and verse text for bible content
            Type = Boolean
        :param parallels: (optional) Comma delimited list of bible_ids to include
            Type = String
        """
        querystring = {
            "content-type": content_type,
            "include-notes": include_notes,
            "include-titles": include_titles,
            "include-chapter-numbers": include_chapter_numbers,
            "include-verse-numbers": include_verse_numbers,
            "include-verse-spans": include_verse_spans,
            "parallels": parallels,
        }
        response = requests.get(
            self.base_url + f"v1/bibles/{bible_id}/sections/{section_id}",
            headers=self.headers,
            params=querystring,
        )
        return json.loads(response.text)["data"]

    def get_chapter_verses(self, bible_id, chapter_id):
        """
        Gets an array of Verse objects for a given bible_id and chapter_id

        :param bible_id: Id of Bible whose verses to fetch
            Type = String
        :param chapter_id: Id of the Chapter whose verses to fetch
            Type = String
        """
        response = requests.get(
            self.base_url + f"v1/bibles/{bible_id}/chapters/{chapter_id}/verses",
            headers=self.headers,
        )
        return json.loads(response.text)["data"]

    def get_verses(
        self,
        bible_id,
        verse_id,
        content_type="html",
        include_notes=False,
        include_titles=False,
        include_chapter_numbers=False,
        include_verse_numbers=False,
        include_verse_spans=False,
        parallels=None,
        use_org_id=False,
    ):
        """
        Gets a Verse object for a given bible_id and verse_id. This
        Verse object also includes an content property with the verse
        corresponding to the verse_id.
        
        :param bible_id: Id of Bible for verses
            Type = String
        :param verse_id: String reference id for the requested verse
            Type = String
        :param content_type: (optional) Content type to be returned in the content property
            Type = String
            Supported Values = [ "html", "json", "text" ]
        :param include_notes: (optional) Include footnotes in content
            Type = Boolean
        :param include_titles: (optional) Include section titles in content
            Type = Boolean
        :param include_chapter_numbers: (optional) Include chapter numbers in content
            Type = Boolean
        :param include_verse_numbers: (optional) Include verse numbers in content
            Type = Boolean
        :param include_verse_spans: (optional) Include spans that wrap verse numbers and verse text for bible content
            Type = Boolean
        :param parallels: (optional) Comma delimited list of bible_ids to include
            Type = String
        :param use_org_id: (optional) Use the supplied id(s) to match the verseOrgId instead of the verseId
            Type = Boolean
        """
        querystring = {
            "content-type": content_type,
            "include-notes": include_notes,
            "include-titles": include_titles,
            "include-chapter-numbers": include_chapter_numbers,
            "include-verse-numbers": include_verse_numbers,
            "include-verse-spans": include_verse_spans,
            "parallels": parallels,
            "use-org-id": use_org_id,
        }
        response = requests.get(
            self.base_url + f"v1/bibles/{bible_id}/verses/{verse_id}",
            headers=self.headers,
            params=querystring,
        )
        return json.loads(response.text)["data"]

    def search(
        self,
        bible_id,
        query,
        limit=10,
        offset=0,
        sort="relevance",
        range=None,
        fuzziness="AUTO",
    ):
        """
        Gets search results for a given bibleId and query string. Searches
        will match all verses with the list of keywords provided in the query string.
        Order of the keywords does not matter. However all keywords must be
        present in a verse for it to be considered a match.
        The total number of results returned from a search can be limited by populating the limit
        attribute in the query string with a non-negative integer value. If no
        limit value is provide a default of 10 is used.
        offset can be used to traverse paginated results. So for example if you are using
        the default limit of 10, using an offset of 10 will return the second page of results,
        namely results 11-20.
        The text property of each verse object contains only the verse text. It does not
        contain footnote references. However, those can be queried directly using the
        /bibles/{bibleId}/verses/{verseId} endpoint.

        :param bible_id: Id of Bible to search
            Type = String
        :param query: Search keywords or passage reference
            Type = String
        :param limit: (optional) Limit for how many matching results to return
            Type = Integer
        :param offset: (optional) Offset for search results. Used to paginate results
            Type = Integer
        :param sort: (optional) Sort order of results
            Type = String
            Supported Values = [ "relevance", "canonical" ]
        :param range: (optional) One or more, comma seperated, passage ids (book, chapter, verse) which the search will be limited to
            Type = String
        :param fuzziness: (optional) Sets the fuzziness of a search to account for misspellings
            Type = String
            Supported Values = [ "0", "1", "2", "AUTO" ]
        """
        querystring = {
            "query": query,
            "limit": limit,
            "offset": offset,
            "sort": sort,
            "range": range,
            "fuzziness": fuzziness,
        }
        respone = requests.get(
            self.base_url + f"v1/bibles/{bible_id}/search",
            headers=self.headers,
            params=querystring,
        )
        return json.loads(respone.text)["data"]

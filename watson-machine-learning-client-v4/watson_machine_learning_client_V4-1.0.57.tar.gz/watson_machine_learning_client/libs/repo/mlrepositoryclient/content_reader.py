################################################################################
#
# Licensed Materials - Property of IBM
# (C) Copyright IBM Corp. 2017
# US Government Users Restricted Rights - Use, duplication disclosure restricted
# by GSA ADP Schedule Contract with IBM Corp.
#
################################################################################


from watson_machine_learning_client.libs.repo.mlrepository import ArtifactReader
import time

class ContentReader(ArtifactReader):
    """
    Reader which read content of pipeline/pipeline model from repository using href.

    :param str content_href: href to content, returned by repository api
    :param MLRepositoryApi: repository api object
    """
    def __init__(self, content_href, repository_api):
        self.content_href = content_href
        self.repository_api = repository_api
        # val apiInvoker: ApiInvoker = repositoryApi.apiInvoker
        # val basePath: String = repositoryApi.basePath
        # var entity: Option[InputStream] = None
        self.connection = None

    def read(self):
        """
        Returns stream object with content of pipeline/pipeline model.

        :return: binary stream
        :rtype: HTTPResponse (from urllib3)
        """
        if self.connection is not None:
            self.close()
        self.connection = self._download()
        return self.connection

    def close(self):  # TODO ????
        """
        Closes stream to content.
        """
        # entity.map(is => is.close())
        self.connection.release_conn()

    def _download(self):
        model_size_1GB = 1073741824
        model_content_size = 0

        if (self.content_href.__contains__("models")):
            return self.repository_api.download_artifact_content(self.content_href, 'false')

        if self.content_href.__contains__("libraries"):
            return self.repository_api.download_artifact_content(self.content_href, 'false', accept='application/gzip')

        if self.content_href.__contains__("runtimes"):
            return self.repository_api.download_artifact_content(self.content_href, 'false', accept='text/plain')
        else:
            #downloading training definition content or modelsize is less than model_size_1GB
            return self.repository_api.download_artifact_content(self.content_href, 'false')

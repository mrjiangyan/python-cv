import sys

from typing import List
from Tea.core import TeaCore

from alibabacloud_facebody20191230.client import Client as FacebodyClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_darabonba_env.client import Client as EnvClient
from alibabacloud_facebody20191230 import models as facebody_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_darabonba_string.client import Client as StringClient
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        region_id: str,
    ) -> FacebodyClient:
        """
        使用AK&SK初始化账号Client
        @param create_client_request_body:
        @return: Facebody
        @throws Exception
        """
        config = open_api_models.Config()
        # 您的AccessKey ID
        config.access_key_id = EnvClient.get_env('ACCESS_KEY_ID')
        # 您的AccessKey Secret
        config.access_key_secret = EnvClient.get_env('ACCESS_KEY_SECRET')
        # 您的可用区ID
        config.region_id = region_id
        return FacebodyClient(config)

    @staticmethod
    def create_face_db(
        client: FacebodyClient,
        db_name: str,
    ) -> None:
        """
        创建人脸数据库
        @param client:
        @param db_name:
        @return: void
        @throws Exception
        """
        try:
            request_body = facebody_models.CreateFaceDbRequest(
                name=db_name
            )
            client.create_face_db(request_body)
            ConsoleClient.log('--------------------创建人脸数据库成功--------------------')
        except Exception as err:
            ConsoleClient.log('create facebody db error')
            ConsoleClient.log(err.message)

    @staticmethod
    async def create_face_db_async(
        client: FacebodyClient,
        db_name: str,
    ) -> None:
        """
        创建人脸数据库
        @param client:
        @param db_name:
        @return: void
        @throws Exception
        """
        try:
            request_body = facebody_models.CreateFaceDbRequest(
                name=db_name
            )
            await client.create_face_db_async(request_body)
            ConsoleClient.log('--------------------创建人脸数据库成功--------------------')
        except Exception as err:
            ConsoleClient.log('create facebody db error')
            ConsoleClient.log(err.message)

    @staticmethod
    def add_face_entity(
        client: FacebodyClient,
        db_name: str,
        entity_id: str,
    ) -> None:
        """
        添加人脸样本
        @param db_name: 数据库名称
        @param entity_id: 实体ID
        @return: void
        @throws Exception
        """
        try:
            request_body = facebody_models.AddFaceEntityRequest()
            request_body.db_name = db_name
            request_body.entity_id = entity_id
            client.add_face_entity(request_body)
            ConsoleClient.log('--------------------创建人脸样本成功--------------------')
        except Exception as err:
            ConsoleClient.log('add face entity error.')
            ConsoleClient.log(err.message)

    @staticmethod
    async def add_face_entity_async(
        client: FacebodyClient,
        db_name: str,
        entity_id: str,
    ) -> None:
        """
        添加人脸样本
        @param db_name: 数据库名称
        @param entity_id: 实体ID
        @return: void
        @throws Exception
        """
        try:
            request_body = facebody_models.AddFaceEntityRequest()
            request_body.db_name = db_name
            request_body.entity_id = entity_id
            await client.add_face_entity_async(request_body)
            ConsoleClient.log('--------------------创建人脸样本成功--------------------')
        except Exception as err:
            ConsoleClient.log('add face entity error.')
            ConsoleClient.log(err.message)

    @staticmethod
    def add_face(
        client: FacebodyClient,
        db_name: str,
        entity_id: str,
        image_url: str,
    ) -> None:
        """
        添加人脸数据
        @param db_name: 数据库名称
        @param entity_id: 实体ID
        @param image_url: 人脸图片地址，必须是同Region的OSS的图片地址。人脸必须是正面无遮挡单人人脸。
        @return: void
        @throws Exception
        """
        try:
            request_body = facebody_models.AddFaceRequest()
            request_body.db_name = db_name
            request_body.entity_id = entity_id
            request_body.image_url = image_url
            client.add_face(request_body)
            ConsoleClient.log('--------------------创建人脸数据成功--------------------')
        except Exception as err:
            ConsoleClient.log('add face error.')
            ConsoleClient.log(err.message)

    @staticmethod
    async def add_face_async(
        client: FacebodyClient,
        db_name: str,
        entity_id: str,
        image_url: str,
    ) -> None:
        """
        添加人脸数据
        @param db_name: 数据库名称
        @param entity_id: 实体ID
        @param image_url: 人脸图片地址，必须是同Region的OSS的图片地址。人脸必须是正面无遮挡单人人脸。
        @return: void
        @throws Exception
        """
        try:
            request_body = facebody_models.AddFaceRequest()
            request_body.db_name = db_name
            request_body.entity_id = entity_id
            request_body.image_url = image_url
            await client.add_face_async(request_body)
            ConsoleClient.log('--------------------创建人脸数据成功--------------------')
        except Exception as err:
            ConsoleClient.log('add face error.')
            ConsoleClient.log(err.message)

    @staticmethod
    def search_face(
        client: FacebodyClient,
        db_name: str,
        image_url: str,
        limit: int,
    ) -> facebody_models.SearchFaceResponse:
        """
        搜索人脸
        @param db_name: 数据库名称
        @param image_url: 图片URL地址。必须是同Region的OSS地址
        @param limit: 搜索结果数量限制
        @return: Facebody.SearchFaceResponse
        @throws Exception
        """
        try:
            request_body = facebody_models.SearchFaceRequest()
            request_body.db_name = db_name
            request_body.image_url = image_url
            request_body.limit = limit
            return client.search_face(request_body)
        except Exception as err:
            ConsoleClient.log('search face error.')
            ConsoleClient.log(err.message)
        return

    @staticmethod
    async def search_face_async(
        client: FacebodyClient,
        db_name: str,
        image_url: str,
        limit: int,
    ) -> facebody_models.SearchFaceResponse:
        """
        搜索人脸
        @param db_name: 数据库名称
        @param image_url: 图片URL地址。必须是同Region的OSS地址
        @param limit: 搜索结果数量限制
        @return: Facebody.SearchFaceResponse
        @throws Exception
        """
        try:
            request_body = facebody_models.SearchFaceRequest()
            request_body.db_name = db_name
            request_body.image_url = image_url
            request_body.limit = limit
            return await client.search_face_async(request_body)
        except Exception as err:
            ConsoleClient.log('search face error.')
            ConsoleClient.log(err.message)
        return

    @staticmethod
    def compare_face(
        client: FacebodyClient,
        image_url_a: str,
        image_url_b: str,
    ) -> facebody_models.CompareFaceResponse:
        """
        人脸比对 1:1
        @param image_url_a: 待比对图片A的URL地址。必须是同Region的OSS地址
        @param image_url_b: 待比对图片B的URL地址。必须是同Region的OSS地址
        @return: Facebody.SearchFaceResponseData
        @throws Exception
        """
        try:
            request_body = facebody_models.CompareFaceRequest()
            request_body.image_urla = image_url_a
            request_body.image_urlb = image_url_b
            return client.compare_face(request_body)
        except Exception as err:
            ConsoleClient.log('compare face error.')
            ConsoleClient.log(err.message)
        return

    @staticmethod
    async def compare_face_async(
        client: FacebodyClient,
        image_url_a: str,
        image_url_b: str,
    ) -> facebody_models.CompareFaceResponse:
        """
        人脸比对 1:1
        @param image_url_a: 待比对图片A的URL地址。必须是同Region的OSS地址
        @param image_url_b: 待比对图片B的URL地址。必须是同Region的OSS地址
        @return: Facebody.SearchFaceResponseData
        @throws Exception
        """
        try:
            request_body = facebody_models.CompareFaceRequest()
            request_body.image_urla = image_url_a
            request_body.image_urlb = image_url_b
            return await client.compare_face_async(request_body)
        except Exception as err:
            ConsoleClient.log('compare face error.')
            ConsoleClient.log(err.message)
        return

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        ConsoleClient.log(args)
        region_id = args[0]
        ConsoleClient.log(region_id)
        db_name = args[1]
        ConsoleClient.log(db_name)
        entity_id = args[2]
        face_url_arr = StringClient.split(args[1], ',', 10)
        test_img_url = args[2]
        ConsoleClient.log(test_img_url)
        # test_compare_img_url = args[3]
        # 获取人脸数据库Client
        client = Sample.create_client(region_id)
        # 创建人脸数据库
        # Sample.create_face_db(client, db_name)
        # 创建人脸样本
        # Sample.add_face_entity(client, db_name, entity_id)
        # 为人脸样本添加图片
        # for url in face_url_arr:
        #     Sample.add_face(client, db_name, entity_id, url)
        # 用测试图片去人脸数据库中查找
        search_face_response = Sample.search_face(client, db_name, test_img_url, 10)
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(search_face_response)))
        # 测试 1:1 人脸比对
        # compare_face_response = Sample.compare_face(client, test_img_url, test_compare_img_url)
        # ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(compare_face_response)))

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        region_id = args[0]
        db_name = args[1]
        entity_id = args[2]
        face_url_arr = StringClient.split(args[1], ',', 10)
        test_img_url = args[2]
        test_compare_img_url = args[3]
        # 获取人脸数据库Client
        client = Sample.create_client(region_id)
        # 创建人脸数据库
        await Sample.create_face_db_async(client, db_name)
        # 创建人脸样本
        await Sample.add_face_entity_async(client, db_name, entity_id)
        # 为人脸样本添加图片
        for url in face_url_arr:
            await Sample.add_face_async(client, db_name, entity_id, url)
        # 用测试图片去人脸数据库中查找
        search_face_response = await Sample.search_face_async(client, db_name, test_img_url, 10)
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(search_face_response)))
        # 测试 1:1 人脸比对
        compare_face_response = await Sample.compare_face_async(client, test_img_url, test_compare_img_url)
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(compare_face_response)))


if __name__ == '__main__':
    Sample.main(sys.argv[1:])

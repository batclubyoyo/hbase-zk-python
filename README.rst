'''
基于 https://github.com/3601314/hbase-python 项目修改而来, 支持 hbase 在 zk 上的根节点路径参数, 其默认根节点为 /hbase
原使用方式: hbase.ConnectionPool(zk).connect()
优化后: hbase.ConnectionPool(zk, "zk_znode_parnet").connect(), 且同时支持原使用方式

项目需要重新打包并上传到服务器进行本地安装, 如下：
打包: pip3 wheel -w target_folder target_path, 会在 target_folder 里生成相应的 whl 安装文件
安装: 将 whl 安装文件上传到服务器, 执行 pip3 install *.whl 进行安装. 安装前需要把原来的 hbase-python 项目通过 pip3 uninstall 卸载掉
'''


hbase-python
^^^^^^^^^^^^

(The development of this package has not finished.)

hbase-python is a python package used to work HBase.

It is now tested under HBase 1.2.6.

Before using HBase, we are familiar with MongoDB and pymongo.
While, when coming to HBase, we found it is not easy to access the database via python.
So, I spent some days to start this project and hope it can be helpful to our daily research work.
The thought of this package comes from "happybase" and "starbase", and I am trying to make the API behaves like
"pymongo".

Dependencies
------------

* Python 3.4+
* requests

Installation
------------

The package can be installed from PyPI repository:

.. code-block:: bash

    pip3 install hbase-python

Examples
--------

Get a row by key:

.. code-block:: python

    import hbase

    zk = 'sis3.ustcdm.org:2181,sis4.ustcdm.org:2181'

    if __name__ == '__main__':
        with hbase.ConnectionPool(zk).connect() as conn:
            table = conn['mytest']['videos']
            row = table.get('00001')
            print(row)
        exit()

Scan a table:

.. code-block:: python

    import hbase

    zk = 'sis3.ustcdm.org:2181,sis4.ustcdm.org:2181'

    if __name__ == '__main__':
        with hbase.ConnectionPool(zk).connect() as conn:
            table = conn['mytest']['videos']
            for row in table.scan():
                print(row)
        exit()

Put a record to a table:

.. code-block:: python

    import hbase

    zk = 'sis3.ustcdm.org:2181,sis4.ustcdm.org:2181'

    if __name__ == '__main__':
        with hbase.ConnectionPool(zk).connect() as conn:
            table = conn['mytest']['videos']
            table.put(hbase.Row(
                '0001', {
                    'cf:name': b'Lily',
                    'cf:age': b'20'
                }
            ))
        exit()

Write a file to a table:

.. code-block:: python

    import hbase

    zk = 'sis3.ustcdm.org:2181,sis4.ustcdm.org:2181'

    if __name__ == '__main__':
        with hbase.ConnectionPool(zk).connect() as conn:
            table = conn['mytest']['videos']
            table.write_file(video_file)  # default filename is "test_video.mp4"
        exit()


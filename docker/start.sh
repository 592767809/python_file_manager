
docker builder prune -f
docker build --no-cache -t python:file_manager .
docker run -itd --name file_manager --net=host --restart=always -v /mnt/vdb1:/srv python:file_manager

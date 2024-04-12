mkdir docker_dir
cd docker_dir
docker run -it --name testing_physics vankaler/physics_lib
docker rm testing_physics
cd ..
rmdir docker_dir
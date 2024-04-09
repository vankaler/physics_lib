mkdir docker_dir
cd docker_dir
docker run -it --name testing_phisics vankaler/physics_lib
docker rm testing_phisics
cd ..
rmdir docker_dir
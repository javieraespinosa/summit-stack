

docker-compose up mysql
ctrl+c

docker-compose up hapi



# Build Tool
cd tag-uploader 
npm i


# Import
node tag-uploader -d generated-sample-data/STU-3/PRO -S http://localhost:8088/fhir
node tag-uploader -d generated-sample-data/STU-3/SYNTHEA -S http://localhost:8088/fhir
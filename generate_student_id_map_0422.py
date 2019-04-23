import csv
import random

def generate_student_id_map(real_student_id, fake_student_id, file_name):
    with open(file_name, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',',
                            quotechar = '|',
                            quoting = csv.QUOTE_MINIMAL)
        # Generate pairs [real_student_id[i], fake_student_id[i]]
        # and save as a row.
        for i in range(len(real_student_id)):
            real_fake_id_pair = [real_student_id[i], fake_student_id[i]]
            writer.writerow(real_fake_id_pair)



if __name__ == "__main__":
    real_student_id = range(0, 300000)
    fake_student_id = range(300000, 600000)
    if len(real_student_id) == len(fake_student_id):
        print("Size match! Continute creating the map.")
        random.shuffle(fake_student_id)
        generate_student_id_map(real_student_id, fake_student_id,
                                'student_id_map_300k_0422.csv')
        print("Map Generated! Done.")
    else:
        print("Size not match! Stop.")

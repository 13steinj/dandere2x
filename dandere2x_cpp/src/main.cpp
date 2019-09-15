#include "Driver.h" //driver_difference
#include "Plugins/Fade/Fade.h"
#include "Image/DebugImage/DebugImage.h"



/*
 * It's a bit messy to leave this here, but this section is dedicated to doing random tests
 * On specific functions for Dandere2x. To use it, simply uncomment //benchmark() in the main class
 * to benchmark or test various features.
 */


void benchmark(){
#include "Image/Image.h"
#include "Plugins/PFrame/PFrame.h"

#include "BlockMatch/ExhaustiveSearch.h"
#include "Image/SSIM/SSIM.h"

    Image im1 = Image("C:\\Users\\windwoz\\Pictures\\test_images\\test_image.png");
    Image im2 = Image("C:\\Users\\windwoz\\Pictures\\test_images\\reallybad.png");

    Image im3 = Image(im1);



    double ssim = SSIM::ssim(im1, im2, 0,0,0,0,30);
    double ssim_copy = SSIM::ssim(im3, im2, 0,0,0,0,30);

    std::cout << "ssim: " << ssim << std::endl;
    std::cout << "ssim copy : " << ssim_copy << std::endl;
}

int main(int argc, char **argv) {

//    benchmark();
//
    bool debug = true; //debug flag

    //Initialize the variables needed for Dandere2x's driver. If debug = True, then we use these variables.

    string workspace = "C:\\Users\\windwoz\\Documents\\sublime_merge\\dandere2x\\src\\workspace\\30_no_fade\\";
    int frame_count = 240;
    int block_size = 20;
    int step_size = 8;
    string run_type = "n";// 'n' or 'r'
    int resume_frame = 55;
    string extension_type = ".jpg";

    cout << "Hello Dandere!!" << endl;

    //load arguments
    if (!debug) {
        workspace = argv[1];
        frame_count = atoi(argv[2]);
        block_size = atoi(argv[3]);
        step_size = atoi(argv[4]);
        run_type = argv[5];
        resume_frame = atoi(argv[6]);
        extension_type = argv[7];
    }

    cout << "Settings" << endl;
    cout << "workspace: " << workspace << endl;
    cout << "frame_count: " << frame_count << endl;
    cout << "block_size: " << block_size << endl;
    cout << "step_size: " << step_size << endl;
    cout << "run_type: " << run_type << endl;
    cout << "ResumeFrame (if valid): " << resume_frame << endl;
    cout << "extension_type: " << extension_type << endl;

    if (run_type == "n")
        driver_difference(workspace, 1, frame_count, block_size, step_size, extension_type);
    else if (run_type == "r")
        driver_difference(workspace, resume_frame, frame_count, block_size, step_size, extension_type);

    return 0;
}

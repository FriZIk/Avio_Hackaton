package com.crafsed.mai_android_application;

import android.content.Intent;
import android.database.Cursor;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Bundle;
import android.provider.OpenableColumns;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import com.bumptech.glide.Glide;

import java.io.File;

import static android.app.Activity.RESULT_OK;

public class LoadFragment extends Fragment {
    interface MListener{
        void send(String s);
        void ok();
    }

    boolean one, two;
    ImageView mImage;;
    TextView mInformation;
    Button mSendButton;
    Button mPhotoLoadButton;
    ImageView mKMLImage;
    private Button mKMLLoadButton;
    private final int GALLERY_REQUEST = 777;
    private final int FILE_SYSTEM_REQUEST = 888;
    MListener mActivity;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable final Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.fragment_load, container, false);
        setHasOptionsMenu(true);
        mImage = v.findViewById(R.id.mainImageView);
        mInformation = v.findViewById(R.id.infoTextView);
        mPhotoLoadButton = v.findViewById(R.id.loadImageButton);
        mKMLLoadButton = v.findViewById(R.id.loadKMLButton);
        mSendButton = v.findViewById(R.id.sendButton);
        mSendButton.setEnabled(false);
        mSendButton.setBackgroundColor(getResources().getColor(R.color.colorInactiveButton,null));
        mKMLImage = v.findViewById(R.id.KMLimage);
        mKMLImage.setVisibility(View.INVISIBLE);


        mImage.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
                intent.setType("image/*");
                startActivityForResult(intent, GALLERY_REQUEST);
            }
        });
        mPhotoLoadButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
                intent.setType("image/*");
                startActivityForResult(intent, GALLERY_REQUEST);
            }
        });
        mKMLLoadButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
                intent.setType("application/vnd.google-earth.kmz");
                startActivityForResult(intent, FILE_SYSTEM_REQUEST);
            }
        });

        mSendButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v){
                mActivity.send(mInformation.getText().toString());

            }
        });

        return v;
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        switch (requestCode){
            case GALLERY_REQUEST:
                if (resultCode==RESULT_OK){
                    Uri selectedImage = data.getData();
                    Glide.with(this).load(selectedImage).centerCrop().into(mImage);
                    Cursor cursor = getContext().getContentResolver().query(selectedImage,null,null,null);
                    int nameIndex = cursor.getColumnIndex(OpenableColumns.DISPLAY_NAME);
                    cursor.moveToFirst();
                    String name = cursor.getString(nameIndex);
                    cursor.close();
                    File f = new File(getContext().getObbDir().getAbsolutePath()+"/"+name);
                    Port.img = f;
                    System.out.println(f.exists());
                    one = true;
                    checkSendButton();
                }
                break;
            case  FILE_SYSTEM_REQUEST:
                if (resultCode==RESULT_OK){
                    Uri selectedFile = data.getData();
                    System.out.println(getContext().getObbDir().getAbsolutePath());
                    mKMLImage.setVisibility(View.VISIBLE);
                    Cursor cursor = getContext().getContentResolver().query(selectedFile,null,null,null);
                    int nameIndex = cursor.getColumnIndex(OpenableColumns.DISPLAY_NAME);
                    cursor.moveToFirst();
                    String name = cursor.getString(nameIndex);
                    cursor.close();
                    String str = Extra.getInstance().unZipper(new File(getContext().getObbDir().getAbsolutePath()+"/"+name));
                    if (str==null){
                        Toast.makeText(getContext(),"Не удалось обработать KMZ файл", Toast.LENGTH_SHORT).show();
                    } else {
                        Port.info = str;
                        mInformation.setText(str);
                    }
                    two = true;
                    checkSendButton();
                }
                break;
        }
    }
    void checkSendButton(){
        if (one&&two){
            mSendButton.setBackgroundColor(getResources().getColor(R.color.colorActiveButton,null));
            mSendButton.setEnabled(true);
        }
    }

}

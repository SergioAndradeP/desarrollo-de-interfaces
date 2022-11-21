package com.example.myothercatalog;

import android.content.Context;
import android.content.Intent;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class SkinViewHolder extends RecyclerView.ViewHolder {
    private ImageView image;
    private TextView name;
    private TextView description;
    private Context context;

    public SkinViewHolder(@NonNull View itemView) {
        super(itemView);
        image = itemView.findViewById(R.id.skin);
        name = itemView.findViewById(R.id.title);
        description = itemView.findViewById(R.id.description);
        context = itemView.getContext();
        itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(context, DetailActivity.class);
                context.startActivity(intent);
            }
        });
    }

    public void ShowData(Skin skin){
        Util.downloadBitmapToImageView(skin.getImageUrl(), this.image);
        this.name.setText(skin.getName());
        this.description.setText(skin.getDescription());
    }
}
